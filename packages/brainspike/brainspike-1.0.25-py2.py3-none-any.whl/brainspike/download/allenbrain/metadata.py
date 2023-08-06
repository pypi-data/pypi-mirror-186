"""
metadata.py

Metadata extraction for human 
patch-clamp aquired data from allen brain. 
https://celltypes.brain-map.org/

"""

import pandas as pd 

import numpy as np 

from ...download.allenbrain.data import AllenBrainData
from ...download.allenbrain.query import AllenBrainQuery

from ...postprocessing.current_steps import calc_current_steps
from ...postprocessing.stimulus_start_end import start_end_stimulus_times

from allensdk.core.cell_types_cache import CellTypesCache
from allensdk.api.queries.cell_types_api import CellTypesApi

###################################################################################################
###################################################################################################

class AllenBrainMetadata(AllenBrainData, AllenBrainQuery): 
    """ parent class for metadata dict from allen brain human neurophysiology dataset of specific specimen ids """
    
    def __init__(self, manifest_file = None, base_uri = None, cache = True, specimen_id = None,\
                    stimulus_type = 'Long Square', file_name = None, require_morphology = False,\
                    require_construction = False, reporter_status = None, simple = True): 
        
        super(AllenBrainData, self).__init__(manifest_file, base_uri, cache,
                                            specimen_id, stimulus_type)

        
        self.manifest_file = manifest_file
        self.file_name = file_name
        self.require_morphology = require_morphology
        self.require_construction = require_construction
        self.reporter_status = reporter_status
        self.simple = simple 
        self.base_uri = base_uri
        self.cache = cache
        self.specimen_id = specimen_id
        self.stimulus_type = stimulus_type
        
        self.ctc = CellTypesCache(cache=self.cache, manifest_file=self.manifest_file, base_uri=self.base_uri)
        self.data_set = self.ctc.get_ephys_data(self.specimen_id) 
        
    @property
    def metadata(self): 
        """ return dict for select specimen id """
        
        if self.specimen_id is not None: 
            
            # isolate specimen id 
            specimen_ids = pd.DataFrame(self.metadata_all)['id'].values
            specimen_id_idx = np.where(specimen_ids == self.specimen_id) 
            
            metadata_dict = self.metadata_all[specimen_id_idx[0][0]]
            
            # + srate 
            #----------
            srate = self.return_srate
            metadata_dict['sample_rate_hz'] = srate
            
            # + current steps 
            #------------------
            index_ranges = self.get_indexrange
            current_steps = calc_current_steps(self.get_commandwaveform, index_ranges=index_ranges)
            metadata_dict['current_step_pa'] = np.diff(current_steps)[0]
            metadata_dict['max_current_step_pa'] = current_steps[-1]
            metadata_dict['min_current_step_pa'] = current_steps[0]
            
            # + stimuli start + end times
            #------------------------------
            start, end = start_end_stimulus_times(self.get_commandwaveform, index_ranges=index_ranges)
            metadata_dict['start_sec'] = index_ranges[0][0]/srate + start/srate
            metadata_dict['end_sec'] = index_ranges[0][0]/srate + end/srate
            metadata_dict['start'] = index_ranges[0][0] + start
            metadata_dict['end'] = index_ranges[0][0] + end
            
            return metadata_dict
        else: 
            raise ValueError(f'specimen id is {self.specimen_id} ...')
        
    @property
    def return_srate(self): 
        """ return sampling rate ::: assumes same params for all sweeps """
        
        sweep_numbers = self._sweep_numbers
        
        srate = self.data_set.get_sweep(sweep_number = sweep_numbers[0])['sampling_rate']

        return srate 
    
