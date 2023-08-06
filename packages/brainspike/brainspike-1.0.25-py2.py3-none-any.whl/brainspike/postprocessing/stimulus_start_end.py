"""
stimulus_start_end.py 

Modules for start and end 
times for stimulus. 

Note: these are assumed to be constant
across all sweepdata.

"""

import numpy as np

###################################################################################################
###################################################################################################

def start_end_stimulus_times(commandwaveform, index_ranges = None): 
    """
    Find start and end stimulus times from 
    command waveform array. 

    Arguments
    ---------
    commandwaveform (arr): 
        arr of depol/hyperpol steps used for stimulus 
        across all sweeps. 
        
    index_ranges (arr): 
        idx of recording to include

    Returns
    -------
    start (float): start of stimulus interval in seconds
    end (float): end of stimulus interval in seconds
    
    """
    
    if index_ranges is not None: 
        start = index_ranges[:,0]
        end = index_ranges[:,1]
    else: 
        start = end = [None]*len(commandwaveform)

    start_set = []; end_set = []
    for count, vals in enumerate(commandwaveform): 
        stimulus_idx = np.nonzero(vals[start[count]:end[count]])
        
        if len(stimulus_idx[0]) > 0: 
            start_set.append(stimulus_idx[0][0])
            end_set.append(stimulus_idx[0][-1])
        else: 
            pass # empty 
        
    # collect unique start times
    start = np.unique(np.array(start_set))
    end= np.unique(np.array(end_set))
    
    # assume equal start, end times across sweeps 
    if (start.size == 1) and (end.size) == 1: 
        return start[0], end[0]
    else: 
        raise ValueError('multiple start and end times found across sweeps ...')
        