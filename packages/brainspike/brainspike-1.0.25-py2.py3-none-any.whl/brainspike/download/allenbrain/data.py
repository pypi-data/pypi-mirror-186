"""
data.py

NWB file extraction for human 
patch-clamp aquired data from allen brain. 
https://celltypes.brain-map.org/

"""

import pandas as pd

import numpy as np 

from allensdk.core.cell_types_cache import CellTypesCache
from allensdk.api.queries.cell_types_api import CellTypesApi
from allensdk.core.cell_types_cache import ReporterStatus as RS
from allensdk.ephys.extract_cell_features import extract_cell_features

from ...utils.core.core_load_utils import (numpy_fillna)

###################################################################################################
###################################################################################################


class AllenBrainData: 
    """ class for download nwb neurophysiology files from allen brain """
    
    def __init__(self, manifest_file = None, base_uri = None, cache = True,\
                specimen_id = None, stimulus_type = 'Long Square'): 
        """ 
        """
        
        self.specimen_id = specimen_id 
        self.cache = cache
        self.manifest_file = manifest_file
        self.base_uri = base_uri
        self.stimulus_type = stimulus_type
        
        self.ctc = CellTypesCache(cache=self.cache, manifest_file=self.manifest_file, base_uri=self.base_uri)
        self.data_set = self.ctc.get_ephys_data(self.specimen_id) 
                
    @property 
    def get_commandwaveform(self): 
        """ return stimuli for sweep numbers """
        
        sweep_numbers = self._sweep_numbers
        
        commandwaveform = []
        for sweep in sweep_numbers: 
            commandwaveform.append(np.array(self.data_set.get_sweep(sweep)['stimulus']*1e12)) # amp -> pA conversion
        return numpy_fillna(commandwaveform)
    
    @property 
    def get_sweepdata(self): 
        """ return sweepdata for sweep numbers """
        
        sweep_numbers = self._sweep_numbers
        
        sweepdata = []
        for sweep in sweep_numbers: 
            sweepdata.append(np.array(self.data_set.get_sweep(sweep)['response']*1e3)) # voltage -> mV conversion
        return sweepdata
    
    @property
    def get_times(self): 
        """ return sweep times """
        
        sweep_numbers = self._sweep_numbers
        
        times= []
        for sweep in sweep_numbers: 
            times.append(np.arange(0,len(self.data_set.get_sweep(sweep)['response']),1)) 
        return times
        
    @property 
    def get_sweepqc(self): 
        """ return seal & initial ra values :: assumes same params for all sweeps """
        
        sweep_numbers = self._sweep_numbers
    
        initial_ra = (self.data_set.get_sweep_metadata(sweep_number = sweep_numbers[0])['initial_access_resistance'])
        seal = (self.data_set.get_sweep_metadata(sweep_number = sweep_numbers[0])['seal'])
        
        return {'initial_ra': initial_ra, 'seal': seal}
    
    @property 
    def get_indexrange(self): 
        """ return index range """
        
        sweep_numbers = self._sweep_numbers
        
        index_range_min = []
        index_range_max = []
        for sweep in sweep_numbers: 
            index_range_min.append(np.array(self.data_set.get_sweep(sweep)['index_range'][0])) 
            index_range_max.append(np.array(self.data_set.get_sweep(sweep)['index_range'][1])) 
        return np.column_stack((index_range_min, index_range_max))
    
    @property
    def _sweep_numbers(self): 
        """ return sweepnumbers for stimulus type """

        stimulus_name = []; sweep_number = []
        for sweep in self.data_set.get_sweep_numbers(): 
            stimulus_name.append(self.data_set.get_sweep_metadata(sweep_number = sweep)['aibs_stimulus_name'])
            sweep_number.append(sweep)
            
        sweep_stim = np.column_stack((sweep_number,stimulus_name))

        return sweep_stim[:,0][np.where(sweep_stim[:,1] == self.stimulus_type)].astype(int)
    