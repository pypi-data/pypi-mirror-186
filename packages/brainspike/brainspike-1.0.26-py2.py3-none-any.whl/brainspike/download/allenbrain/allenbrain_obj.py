"""
data_obj.py

Class for Allen Brain data object
containing data and metadata. 

"""

from .metadata import AllenBrainMetadata

###################################################################################################
###################################################################################################

class AllenBrain(AllenBrainMetadata): 
    
    """
    Parent class for Allen Brain data and metadata
    inheritance from a single stimulus type.  
    """

    def __init__(self, manifest_file = None, base_uri = None, cache = True, specimen_id = None,\
                    stimulus_type = 'Long Square', file_name = None, require_morphology = False,\
                    require_construction = False, reporter_status = None, simple = True): 
        """
        """

        super().__init__(manifest_file, base_uri, cache, specimen_id, stimulus_type, file_name,\
                        require_morphology, require_construction, reporter_status, simple)
                 

        self.sweepdata = self.get_sweepdata
        self.commandwaveform = self.get_commandwaveform
        self.times = self.get_times/self.return_srate
        self.sweepqc = self.get_sweepqc