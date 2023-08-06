"""
plot_utils.py 

General modules for plots. 

"""

import numpy as np 

###################################################################################################
###################################################################################################

def moving_average(x, w):
    
    return np.convolve(x, np.ones(w), 'same') / w  

def smooth_data(data, smooth_window = 2): 
    
    smooth_data = moving_average(data, smooth_window) 
    # smooth_data = np.insert(smooth_data, 0, 0) # default to zero

    return smooth_data 