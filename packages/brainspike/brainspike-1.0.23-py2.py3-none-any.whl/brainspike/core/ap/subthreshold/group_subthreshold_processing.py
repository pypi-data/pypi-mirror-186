""" 
group_subthreshold_processing.py 

Class for group data subthreshold feature 
extractions.

"""

import pandas as pd 

import numpy as np 

from .subthreshold_processing import (SubthresholdFeatures)

from ....exporters.dataframes import (export_df)

###################################################################################################
###################################################################################################

class SubthresholdGroupFeatures(SubthresholdFeatures): 
    """ class for group subthreshold feature extractions """
    
    def __init__(self, data = None, baseline_interval_sub = 0.1, peak_width = 0.005, rms_cutoff_sub = 0.2,\
                    sag_amp_threshold = [-5, -200], r2_cutoff_sub = 0.8, deflect_window = 0.2, group_data = None): 
        """
        """
        
        super().__init__(data, baseline_interval_sub, peak_width, rms_cutoff_sub,\
                            sag_amp_threshold, r2_cutoff_sub, deflect_window)
        
        self.group_data = group_data
        
        
    def group_df_subthreshold(self, i_search = -80, fdir = 'processed/subthreshold/df_subthreshold/master',\
                                fname = 'df_subthreshold'): 
        """ return group df for all subthreshold features """
        
        df = pd.DataFrame() 
        
        if self.group_data is not None: 
            for data in self.group_data: 
                
                self.data = data 
                
                df_subthreshold_main = self.df_subthreshold_main(i_search = i_search)

                df = df.append(df_subthreshold_main, ignore_index = False)    
        
        else: 
            raise ValueError(f'pass group data objects | group_data: {self.group_data} ...')
        
        if fdir is not None: 
            export_df(data = self.data, df = df, fdir = fdir, fname = fname, file_extension = '.xlsx') 
        else: 
            pass
        
        return df 
        
        
    def group_export_all_sag_features(self, fdir = 'processed/subthreshold/df_all_sag_features', file_extension = '.xlsx'): 
        """ export all sag features for data group """
        
        if self.group_data is not None: 
            for data in self.group_data: 
                
                self.data = data 
                
                if fdir is not None: 
                    fname = data.metadata['abf_id'] # default to abf id 
                    self.df_all_sag_features(fdir = fdir, fname = fname, file_extension = file_extension) # export on each iteration 
                else: 
                    raise ValueError('pass a file directory for export | fdir: {fdir} ...')

            print('finished exporting all sag features ...')
            
        else: 
            raise ValueError(f'pass group data objects | group_data: {self.group_data} ...')
        
        
    def group_export_sag_plots(self, figdir = 'figures/subthreshold/sag', file_extension = '.pdf', xlim = None, scale_bar = False): 
        """ export all sag plots for selected 'stable' sweeps """
        
        if self.group_data is not None: 
            for data in self.group_data: 
                
                self.data = data 
                self.df_all_sag_features() # process features
                
                if (len(self.adjusted_sweepnumbers_sub) > 0): 
                    figname = self.data.metadata['abf_id']
                    
                    if xlim is None: 
                        xlim = [self.start - 0.2, self.end + 0.2]
                    else: 
                        pass 
                        
                    self.plot_sag(sweeps = self.adjusted_sweepnumbers_sub[self.stable_sweepidx_sub[0]], deflect_v = True, xlim = xlim,\
                                    ylim_v = None, ylim_i = None, scale_bar = scale_bar, axis = False,\
                                    figdir = figdir, figname = figname, figextension = file_extension)
                else: 
                    pass # no depolarizing sweeps found
        else: 
            raise ValueError(f'pass group data objects | group_data: {self.group_data} ...')