"""
rheobase.py

Modules to find rheobase 
for sweep level spike analysis. 

"""

import numpy as np 
from numpy.lib.stride_tricks import sliding_window_view as window

import pandas as pd 

###################################################################################################
###################################################################################################

def return_rheobase(df_spiketrain): 
    """ returns rheobase (pA) from sweep train feature extractions (all sweeps) """

    if ~np.isnan(df_spiketrain['avg_rate'].values[0]): 
        
        avg_rate = df_spiketrain['avg_rate'].values
        sweep_numbers = np.unique(df_spiketrain['sweep_number_supra'].values)
        
        try: 
            rheobase_idx = np.where(avg_rate != 0)[0][0] # first idx != 0 pA stimuli

            if (rheobase_idx > 0) and (avg_rate[rheobase_idx-1] == 0):
            
                rheobase_df = df_spiketrain[df_spiketrain['sweep_number_supra'] == sweep_numbers[rheobase_idx]]
                rheobase = rheobase_df.stimulus.values[0]
                rheobase_sweepnumber = rheobase_df.sweep_number_supra.values[0]
                
                return rheobase, rheobase_sweepnumber
            else: 
                return 0, 0 # no rheobase :: firing @ baseline
        except: 
            return np.nan, np.nan # no rheobase found 
    else: 
        return np.nan, np.nan # no rheobase :: no depol steps 