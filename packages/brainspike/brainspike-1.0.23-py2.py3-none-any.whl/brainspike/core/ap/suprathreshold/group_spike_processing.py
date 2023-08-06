""" 
group_spike_processing.py 

Class for group data spike feature 
extractions + plots. 

"""

import pandas as pd 

import numpy as np 

from .spike_processing import (SpikeFeatures)

from ....exporters.dataframes import (export_df)
from ....plots.group_spike_plot import (group_i_f_plot, group_spike_plot)

###################################################################################################
###################################################################################################

class SpikeGroupFeatures(SpikeFeatures): 
    """ class for group spike feature extractions """
    
    def __init__(self, data = None, dv_cutoff=5., max_interval=0.005, min_height = 2., min_peak = 0.,\
                thresh_frac = 0.05, reject_at_stim_start_interval = 0, baseline_interval = 0.05, rms_cutoff = 2,\
                burst_tol = 0.5, pause_cost = 1.0, group_data = None): 
        """
        """
        
        super().__init__(data, dv_cutoff, max_interval, min_height, min_peak,\
                thresh_frac, reject_at_stim_start_interval, baseline_interval, rms_cutoff,\
                burst_tol, pause_cost)
        
        self.group_data = group_data
        
        
    def group_df_spike_main(self, sweep_search = 'max_firing', i_search = None, fdir = None, fname = None): 
        """ return group df for all main spike features """
        
        df = pd.DataFrame() 
        
        if self.group_data is not None: 
            for data in self.group_data: 
                
                self.data = data 
                
                df_spikes_main = self.df_spikes_main(sweep_search = sweep_search, i_search = i_search)
                df = df.append(df_spikes_main, ignore_index = False)  

        else: 
            raise ValueError(f'pass group data objects | group_data: {self.group_data} ...')
        
        if fdir is not None: 
            export_df(data = self.data, df = df, fdir = fdir, fname = fname, file_extension = '.xlsx') 
        else: 
            pass
        
        return df 
    
    
    def group_export_all_spike_features(self, fdir = 'processed/spikes/df_all_spikes_features', file_extension = '.xlsx'): 
        """ export all spike features for data group across all sweeps """
        
        if self.group_data is not None: 
            for data in self.group_data: 
                
                self.data = data 
                
                if fdir is not None: 
                    fname = data.metadata['abf_id'] # default to abf id 
                    self.df_spikes_allsweeps(fdir = fdir, fname = fname, file_extension = file_extension) # export on each iteration 
                else: 
                    raise ValueError('pass a file directory for export | fdir: {fdir} ...')

            print('finished exporting all spike features ...')
            
        else: 
            raise ValueError(f'pass group data objects | group_data: {self.group_data} ...')
        
        
    def group_export_all_spiketrain_features(self, fdir = 'processed/spiketrain/df_all_spiketrain_features', file_extension = '.xlsx'): 
        """ export all spiketrain features for data group across all sweeps """
        
        if self.group_data is not None: 
            for data in self.group_data: 
                
                self.data = data 
                
                if fdir is not None: 
                    fname = data.metadata['abf_id'] # default to abf id 
                    self.df_spiketrain_allsweeps(fdir = fdir, fname = fname, file_extension = file_extension) # export on each iteration 
                else: 
                    raise ValueError('pass a file directory for export | fdir: {fdir} ...')

            print('finished exporting all spiketrain features ...')
            
        else: 
            raise ValueError(f'pass group data objects | group_data: {self.group_data} ...')
        
        
    def group_plot_i_f(self, figdir = None, figname = None, figextension = None, smooth_window = None): 
        """ group plot for i-f relationships """
        
        if self.group_data is not None: 
            
            f = []; i = []
            for data in self.group_data: 
                
                self.data = data   
                df_spiketrain = self.process_spiketrain
                df_spiketrain = df_spiketrain[df_spiketrain['avg_rate'].notna()]

                if len(df_spiketrain) > 0: # skip sweepdata with no depol steps
                    f.append(df_spiketrain['avg_rate'].values)
                    i.append(df_spiketrain['stimulus'].values)
                else: 
                    pass
                
            i = np.concatenate([x.ravel() for x in i])
            f = np.concatenate([x.ravel() for x in f])

            unique_i, idx_i, counts_i = np.unique(i, return_inverse=True, return_counts=True)
            mean_f = np.bincount(idx_i, weights=f) / counts_i
            
            stds = np.array([np.std(f[i==u]) for u in unique_i])
            size = np.array([np.size(f[i==u]) for u in unique_i])
            sem = stds/np.sqrt(size)
            
            group_i_f_plot(i = unique_i, f = mean_f, sem = sem, smooth_window = smooth_window,\
                            figdir = figdir, figname = figname, figextension = figextension)
    
        else: 
            raise ValueError(f'pass group data objects | group_data: {self.group_data} ...')     
        
        
    def group_plot_max_spike(self, slice_window = [-0.008, 0.01], scale_bar = True, axis = False,\
                            figdir = None, figname = None, figextension = None, ylim_v = [-90, 70],\
                            ylim_phase = [None, None], xlim_phase = [None, None]): 
        """ group plot for peak spike on max firing sweep """
        
        if self.group_data is not None: 
            
            v = []; peak_v_deriv = []
            for data in self.group_data: 
                
                self.data = data   
                df_max_firing = self.df_spikes_main(sweep_search = 'max_firing', i_search = None)
                
                if ~np.isnan(df_max_firing.sweep_number_supra.values[0][0]): 
                    max_firing_sweep = df_max_firing.sweep_number_supra.values[0][0]
                    max_peak_index = df_max_firing.peak_index.values[0]
                    
                    v_slice = self.sweepdata[max_firing_sweep][max_peak_index+int(slice_window[0]*self.srate):max_peak_index+int(slice_window[1]*self.srate)]
                    
                    v.append(v_slice)
                    peak_v_deriv.append(np.diff(v_slice) * (self.srate/1000))
                else: 
                    pass 
                
            t = np.arange(slice_window[0], slice_window[1], 1/self.srate)
            v_mean = np.mean(np.squeeze(v), axis = 0)
            peak_v_deriv = np.mean(np.squeeze(peak_v_deriv), axis = 0)
            
            sem_v = np.std(np.squeeze(v), ddof=1, axis = 0)/np.sqrt(np.size(np.squeeze(v)))
            sem_v_deriv = np.std(np.squeeze(peak_v_deriv), ddof=1, axis = 0)/np.sqrt(np.size(np.squeeze(peak_v_deriv)))
            
            group_spike_plot(t = t, v = v_mean, peak_v_deriv = peak_v_deriv, sem_v = sem_v, sem_v_deriv = sem_v_deriv, min_peak = self.min_peak,\
                            scale_bar = scale_bar, axis = axis, figdir = figdir, figname = figname, figextension = figextension,\
                            ylim_v = ylim_v, ylim_phase = ylim_phase, xlim_phase = xlim_phase)
        else: 
            raise ValueError(f'pass group data objects | group_data: {self.group_data} ...') 
        

    def group_export_maxfiring_plots(self, figdir = 'figures/spiketrain/max_ap', figextension = '.pdf',\
                                    show_all_stable = False, scale_bar = True, axis = False,\
                                    features = ['max_ap_index', 'peak_index']): 
        """ export all spiketrain plots on max firing sweeps """
        
        if self.group_data is not None: 
            for data in self.group_data: 
                
                self.data = data 
                
                df_max_firing = self.df_spikes_main(sweep_search = 'max_firing', i_search = None)
                max_firing_sweep = df_max_firing.sweep_number_supra.values[0]

                if figdir is not None: 
                    figname = data.metadata['abf_id'] + '_sweep_' + str(max_firing_sweep) # default to abf id + sweep \
                    
                    if features is None: 
                        features = ['max_ap_index', 'peak_index', 'upstroke_index', 'downstroke_index',\
                                    'threshold_index','slow_trough_index', 'fast_trough_index', 'trough_index'] # default to all 
                    else: 
                        pass 
                    
                    self.plot_spiketrain(sweeps = [max_firing_sweep], features = features, figdir = figdir,\
                        figname = figname, figextension = figextension,show_all_stable = show_all_stable,\
                        xlim = [self.start - 0.2, self.end + 0.2], scale_bar = scale_bar, axis = axis) # export on each iteration 
                else: 
                    raise ValueError('pass a file directory for export | fdir: {fdir} ...')

            print('finished exporting all spiketrain figure plots ...')
            
        else: 
            raise ValueError(f'pass group data objects | group_data: {self.group_data} ...')
    
    