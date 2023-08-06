""" 
core_load_utils.py 

Modules for general collection 
of data from data objects for 
core classes. 

"""

import numpy as np 

###################################################################################################
###################################################################################################


def find_sweepdata(data): 
    """ find sweepdata """

    try: 
        sweepdata = data.preprocessed_sweepdata # find preprocessed data 
    except:
        try: 
            sweepdata = data.sweepdata # if not, default to raw 
        except: 
            id = data.metadata['id']
            print(f'no data found for {id}| re-load data with loader ...')   
        
    # note: to only be conducted in 
    # recordings from current clamp
    # with multiple sweep data
    #--------------------------------
    if len(sweepdata) > 1: 
        pass
    else: 
        raise ValueError('pass sweepdata | multiple sweeps not found ...')
        
    return sweepdata
        
        
def find_sweeptimes(data): 
    """ find sweep times """

    try: 
        sweeptimes = data.times # find preprocessed data 
    except:
        id = data.metadata['id']
        print(f'check sweepdata times for {id} ...')
        
    # note: to only be conducted in 
    # recordings from current clamp
    # with multiple sweep data
    #--------------------------------
    if len(sweeptimes) > 1: 
        pass
    else: 
        raise ValueError('pass sweepdata | multiple sweeps not found ...')       
    
    return sweeptimes
    
    
def find_stimuli(data): 
    """ find current stimuli """
    
    try: 
        stimuli = data.commandwaveform        
    except: 
        raise ValueError('no stimuli data found ...')
    
    return stimuli


def find_srate(data): 
    """ find sampling rate frequency """
    
    try: 
        srate = data.metadata['sample_rate_hz']
    except AttributeError:
        id = data.metadata['id']
        print(f'no sampling rate found for {id}| re-load data with loader ...')   
        
    return srate 


def numpy_fillna(data):
    """ fill rows with zeros if different lengths across sweeps in stack """
    
    # Get lengths of each row of data
    lens = np.array([len(i) for i in data])

    # Mask of valid places in each row
    mask = np.arange(lens.max()) < lens[:,None]

    # Setup output array and put elements from data into masked positions
    out = np.zeros(mask.shape)
    out[mask] = np.concatenate(data)
    
    return out