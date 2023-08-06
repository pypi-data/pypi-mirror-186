"""
query.py

Class for querying allen brain database 
neurophysiology data. 

"""

from allensdk.core.cell_types_cache import CellTypesCache
from allensdk.api.queries.cell_types_api import CellTypesApi

###################################################################################################
###################################################################################################

class AllenBrainQuery: 
    """ class for returning metadata dict from allen brain human neurophysiology database """
    
    def __init__(self, file_name = None, manifest_file = None, require_morphology = False, require_construction = False,\
                    reporter_status = None, simple = True, base_uri = None, cache = True, specimen_id = None, stimulus_type = 'Long Square'): 
        
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
        
    @property
    def metadata_all(self): 
        """ return metadata dict for all human recordings """

        metadata_dict = self.ctc.get_cells(file_name=self.file_name, require_morphology=self.require_morphology,\
                            require_reconstruction=self.require_construction,\
                            reporter_status=self.reporter_status, species=[CellTypesApi.HUMAN],\
                            simple=self.simple)
        
        return metadata_dict 