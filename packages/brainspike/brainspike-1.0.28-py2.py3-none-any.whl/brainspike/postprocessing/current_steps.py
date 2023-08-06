"""
current_steps.py 

Modules for finding current steps
from current arrays. 

"""

import numpy as np

###################################################################################################
###################################################################################################

def calc_current_steps(commandwaveform, index_ranges = None, start = None, end = None): 
    """
    
    Returns arr of command waveform injected per step (pA) 
    and the index of injection start. 
    
    Arguments
    ---------
    commandwaveform (arr): 
        arr of depol/hyperpol steps used for stimulus 
        across all sweeps. 

    index_ranges (arr): 
        idx of recording to include
        
    Returns
    -------
    current_steps (arr): 
        current step per sweep
    
    Raises
    ------
    CurrentCheck: 
        no current stimulus found
        
    References: 
    -----------
    https://github.com/AllenInstitute/AllenSDK/blob/9ef5214dcb04a61fe4c04bf19a5cb13c9e1b03f1/allensdk/core/nwb_data_set.py#L40

    """
    
    if (start is not None) and (end is not None): 
        start = [start]*len(commandwaveform)
        end = [end]*len(commandwaveform)
        
    elif index_ranges is not None: 
        start = index_ranges[:,0]
        end = index_ranges[:,1]
        
    else: 
        start = end = [None]*len(commandwaveform)
        
    current_steps = []
    for count, vals in enumerate(commandwaveform): 
        step_calc_max = np.amax(vals[start[count]:end[count]]) # max current injection (+ve polarity)
        step_calc_min = np.amin(vals[start[count]:end[count]]) # min current injection (-ve polarity) 
        current_steps.append(step_calc_max - abs(step_calc_min))  # current delta 

    return current_steps 


