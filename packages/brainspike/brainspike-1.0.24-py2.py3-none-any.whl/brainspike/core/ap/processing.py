"""
processing.py

Parent class for detecting spike and subthreshold features
in action potential sweepdata. 

Note: spike feature extraction modules adapted from iPFX
[https://github.com/AllenInstitute/ipfx/tree/797e677070ff161960bf72c97d70b40b91aef74a]

"""

import numpy as np 

import pandas as pd 

from .subthreshold.group_subthreshold_processing import (SubthresholdGroupFeatures)
from .suprathreshold.group_spike_processing import (SpikeGroupFeatures)
from ...exporters.dataframes import (export_df)

###################################################################################################
###################################################################################################

class APFeatures(SubthresholdGroupFeatures, SpikeGroupFeatures): 
    """ class for supra and sub feature extractions """
    
    def __init__(self, data = None, baseline_interval_sub = 0.1, peak_width = 0.005, sag_amp_threshold = [-5, -200], r2_cutoff_sub = 0.8,\
                rms_cutoff_sub = 0.2, deflect_window = 0.2, dv_cutoff = 5., max_interval=0.005, min_height = 2., min_peak = 0.,\
                thresh_frac = 0.05, reject_at_stim_start_interval = 0, baseline_interval = 0.05,\
                rms_cutoff = 10, burst_tol = 0.5, pause_cost = 1.0, group_data = None): 
        """
        """
        
        self.data = data
        self.group_data = group_data
        self.rms_cutoff_sub = rms_cutoff_sub
        self.baseline_interval_sub = baseline_interval_sub
        self.peak_width = peak_width 
        self.sag_amp_threshold = sag_amp_threshold
        self.r2_cutoff_sub = r2_cutoff_sub
        self.deflect_window = deflect_window
        self.dv_cutoff = dv_cutoff
        self.max_interval = max_interval
        self.min_height = min_height
        self.min_peak = min_peak
        self.thresh_frac = thresh_frac
        self.reject_at_stim_start_interval = reject_at_stim_start_interval
        self.baseline_interval = baseline_interval
        self.rms_cutoff = rms_cutoff
        self.burst_tol = burst_tol
        self.pause_cost = pause_cost
        
        
    def group_sub_supra_df(self, sweep_search = 'max_firing', i_search_supra = None, i_search_sub = -80,\
                            fdir = None, fname = None): 
        """ return group df for all supra + subthreshold feature extractions """
        
        df = pd.DataFrame() 
        
        if self.group_data is not None: 
            for data in self.group_data: 
                
                self.data = data 

                sub_supra_df = self.sub_supra_df(sweep_search = sweep_search, i_search_supra = i_search_supra,\
                                                i_search_sub = i_search_sub)
                df = df.append(sub_supra_df, ignore_index = False)    
        else: 
            raise ValueError(f'pass group data objects | group_data: {self.group_data} ...')
        
        if fdir is not None: 
            export_df(data = self.data, df = df, fdir = fdir, fname = fname, file_extension = '.xlsx') 
        else: 
            pass
        
        return df 
        
        
    def sub_supra_df(self, sweep_search = 'max_firing', i_search_supra = None, i_search_sub = -80,\
                    fdir = None, fname = None): 
        """ return combined feature extaction for supra and sub features from single recording """
        
        df_spikes_main = self.df_spikes_main(sweep_search = sweep_search, i_search = i_search_supra) # supra features 
        df_subthreshold_main = self.df_subthreshold_main(i_search = i_search_sub) # sub features 
        
        df_main = pd.concat([df_spikes_main, df_subthreshold_main], axis=1, join='inner')
        
        _, idx = np.unique(df_main.columns, return_index=True)
        df_main = df_main.iloc[:, np.sort(idx)] 
        
        if fdir is not None: 
            export_df(data = self.data, df = df_main, fdir = fdir, fname = fname, file_extension = '.xlsx') 
        else: 
            pass
        
        return df_main