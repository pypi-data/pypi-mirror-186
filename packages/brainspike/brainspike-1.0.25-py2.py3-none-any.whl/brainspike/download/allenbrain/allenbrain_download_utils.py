"""
allenbrain_download_utils.py

Modules for extracting additional 
metadata from allen brain nwb files. 

"""

import numpy as np 

import pandas as pd 

from ...download.allenbrain.data import AllenBrainData

###################################################################################################
###################################################################################################

def get_srate(id = None, manifest_file = None, stimulus_type = None): 
    """ return sampling rate for sweep data """
    
    allenbrain_data = AllenBrainData(specimen_id = id,\
                                    manifest_file = manifest_file,\
                                    stimulus_type = stimulus_type)

    sweep_numbers = allenbrain_data._sweep_numbers
    
    srate = allenbrain_data.data_set.get_sweep(sweep_number = sweep_numbers[0])['sampling_rate']
    
    print(srate)

    return srate 