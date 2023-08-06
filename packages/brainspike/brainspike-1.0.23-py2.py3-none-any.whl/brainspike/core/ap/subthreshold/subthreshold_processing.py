"""
subthrshold_processing.py

Class for detecting subthreshold features
(hyperpolarizing sweepdata) + plots. 

Note: subthreshold feature extraction modules adapted from iPFX
[https://github.com/AllenInstitute/ipfx/tree/797e677070ff161960bf72c97d70b40b91aef74a]

"""

import pandas as pd 

import numpy as np 

from ..suprathreshold.spike_processing import (SpikeFeatures) 

from ....abf.abf_obj import (ABF)
from ....features.ipfx.subthresh_features import (voltage_deflection, sag, input_resistance)
from ....curation.subthresh_sweepdata_qc import (drop_unstablesweeps_rms, drop_depolsweeps, measure_linregress)
from ....plots.subthreshold_qc_plots import (ri_plot)
from ....plots.subthreshold_plots import (sag_plot, subthreshold_plot_allsweeps)
from ....exporters.dataframes import (export_df)
from ....utils.core.core_load_utils import (find_srate, find_stimuli, find_sweepdata, find_sweeptimes)

###################################################################################################
###################################################################################################

class SubthresholdFeatures(SpikeFeatures): 
    
    """ class for detecting sag current features in ap sweep data """
    
    def __init__(self, data, baseline_interval_sub = 0.1, peak_width = 0.005, rms_cutoff_sub = 0.2,\
                sag_amp_threshold = [-5, -200], r2_cutoff_sub = 0.8, deflect_window = 0.2, dv_cutoff=5., max_interval=0.005, min_height = 2.,\
                min_peak = 0., thresh_frac = 0.05, reject_at_stim_start_interval = 0, baseline_interval = 0.05, rms_cutoff = 2,\
                burst_tol = 0.5, pause_cost = 1.0): 
        """
        """
        
        self.baseline_interval_sub = baseline_interval_sub 
        self.peak_width = peak_width
        self.rms_cutoff_sub = rms_cutoff_sub
        self.sag_amp_threshold = sag_amp_threshold
        self.r2_cutoff_sub = r2_cutoff_sub
        self.filtered_amp_idx = None 
        self.deflect_window = deflect_window
        self.data = data 
        
        super().__init__(data, dv_cutoff, max_interval, min_height, min_peak,\
                thresh_frac, reject_at_stim_start_interval, baseline_interval, rms_cutoff,\
                burst_tol, pause_cost)
        
        
    @property
    def process_sag(self): 
        """ find sag features across all sweepdata for a single voltage recording """
        
        try: 
            isinstance(self.data, ABF)
            self.sweeptimes_sub = find_sweeptimes(self.data)
            self.sweepdata_sub = find_sweepdata(self.data)
            self.stimuli_sub = find_stimuli(self.data)
            self.srate = find_srate(self.data)
            self.start = self.data.metadata['start_sec'] # start + end stimuli (seconds)
            self.end = self.data.metadata['end_sec']
            self._sweep_qc_sub
            
        except AttributeError: 
            raise AttributeError("pass single data object ...")   
        
        # find sag and voltage deflections
        #----------------------------------
        # iterate across all 'stable' sweeps 

        if (len(self.stable_sweepdata_sub) > 0) and (len(self.adjusted_sweepnumbers_sub) > 0): 
            
            df_sag_all_sweeps = pd.DataFrame()
            
            deflect_vset = []; deflect_indexset = []; sag_values = []; # better way to do this? 
            sag_voltages_fromsteady = []; sag_currentsteps = []; 
            for t, v, i in zip(self.stable_sweeptimes_sub, self.stable_sweepdata_sub, self.stable_stimuli_sub): 
        
                # voltage_deflection
                #--------------------
                deflect_v, deflect_index = voltage_deflection(t,v,i, start = self.start,\
                                            end = self.start + self.deflect_window, deflect_type = "min") # ipfx src code 
                
                # sag feature extraction
                #-----------------------
                sag_value, sag_voltage_fromsteady = sag(t,v,i, start = self.start, end = self.end,\
                                                        peak_width=self.peak_width,\
                                                        baseline_interval=self.baseline_interval_sub) # ipfx src code 
                
                # remove low amplitude sag 
                #--------------------------
                # filter sag between amp cutoffs
                # note: sag voltage must be a negative value
                
                if (sag_voltage_fromsteady < self.sag_amp_threshold[1]) | (sag_voltage_fromsteady > self.sag_amp_threshold[0]):
                    sag_value = 0 # default :: 0 mV 
                    sag_voltage_fromsteady = 0 
                else: 
                    pass 
   
                deflect_vset.append(deflect_v) 
                deflect_indexset.append(deflect_index)
                sag_values.append(sag_value)
                sag_voltages_fromsteady.append(sag_voltage_fromsteady)
                sag_currentsteps.append(min(i))
                
            ##################
            # sag feature df 
            ##################
            # output df for all sag features 
            # across stable sweeps 

            df_sag_all_sweeps['sweep_number_sub'] = self.adjusted_sweepnumbers_sub[self.stable_sweepidx_sub[0]]
            df_sag_all_sweeps['deflect_v'] = np.array(deflect_vset)
            df_sag_all_sweeps['deflect_index'] = np.array(deflect_indexset)
            df_sag_all_sweeps['sag_values'] = np.array(sag_values)
            df_sag_all_sweeps['sag_voltages_fromsteady'] = np.array(sag_voltages_fromsteady)
            df_sag_all_sweeps['sag_currentsteps'] = np.array(sag_currentsteps)
                                      
        else:
            df_sag_all_sweeps = pd.DataFrame({'sweep_number_sub': np.nan, 'deflect_v': np.nan, 'deflect_index': np.nan,\
                                            'sag_values': np.nan, 'sag_voltages_fromsteady': np.nan,\
                                            'sag_currentsteps': np.nan, 'sweep_number_sub': np.nan},\
                                            index = [0]) # empty df 
            
        return df_sag_all_sweeps
    

    @property
    def process_inputresistance(self): 
        """ find imput resistance for all sweeps """
        
        df_sag_all_sweeps = self.process_sag
        
        if len(self.stable_sweeptimes_sub) >= 3: 
            try: 
                v_peak = df_sag_all_sweeps['deflect_v'].values
                i = df_sag_all_sweeps['sag_currentsteps'].values
                
                linregress_dict = measure_linregress(i = i, v = v_peak) # check linearity 

                if linregress_dict['r2_value'] >= self.r2_cutoff_sub: 
                    ri = input_resistance(self.stable_sweeptimes_sub, self.stable_stimuli_sub,\
                                            self.stable_sweepdata_sub, start = self.start, end = self.end,\
                                                baseline_interval = self.baseline_interval_sub)
                    return ri, linregress_dict['r2_value']
                else: 
                    return np.nan, linregress_dict['r2_value'] # if < r2 value cutoff 
            except: 
                return np.nan, np.nan   
        else: 
            return np.nan, np.nan  # sanity check :: < 3 sweeps // insufficient to calc. Ri 
            
          
    def df_subthreshold_main(self, i_search = -80, fdir = None, fname = None, file_extension = '.xlsx'): 
        """ sag features + ri + qc + detection parameters for select sweep with export option """
        
        if (i_search is not None) and (isinstance(i_search, int)): 
        
            df = pd.DataFrame(index = [self.data.metadata['abf_id']]) 
            
            # process sag features 
            df_sag_all_sweeps = self.process_sag
            
            # find values closest to i_search 
            # default set at -80 mV for HCN current
            #---------------------------------------
            sag_currentsteps = df_sag_all_sweeps['sag_currentsteps'].values
            sag_currentsteps_min_idx = np.absolute(sag_currentsteps - (i_search)).argmin()

            if sag_currentsteps_min_idx.size == 1: 
                
                # + metadata 
                df = pd.concat([pd.DataFrame(self.data.metadata,\
                    index = [self.data.metadata['abf_id']]), df], axis = 1, ignore_index = False)

                # + preprocessing params 
                try: 
                    self.data.preprocessed_params
                    df = pd.concat([df, pd.DataFrame(self.data.preprocessed_params,\
                        index = [self.data.metadata['abf_id']])], axis = 1, ignore_index = False)
                except: 
                    pass 
            
                # + detection parameters 
                df['baseline_interval_sub'] = self.baseline_interval_sub
                df['peak_width'] = self.peak_width
                df['rms_cutoff_sub'] = self.rms_cutoff_sub
                df['sag_amp_threshold_min'] = self.sag_amp_threshold[0]
                df['sag_amp_threshold_max'] = self.sag_amp_threshold[1]
                df['i_search_sub'] = i_search 
                df['r2_cutoff_sub'] = self.r2_cutoff_sub
            
                # + qc parameters
                df['total_sweep_count'] = len(self.sweepdata_sub)
                df['analysed_sweep_count'] = len(self.stable_sweepdata_sub)
                df['stable_sweep_currentsteps'] = [sag_currentsteps]
                
                # + sag values closest to i search 
                df['sag_currentstep'] = sag_currentsteps[sag_currentsteps_min_idx]
                df['sag_value'] = df_sag_all_sweeps['sag_values'].values[sag_currentsteps_min_idx]
                df['deflect_index'] = df_sag_all_sweeps['deflect_index'].values[sag_currentsteps_min_idx]
                df['deflect_v'] = df_sag_all_sweeps['deflect_v'].values[sag_currentsteps_min_idx]
                df['sweep_number_sub'] = df_sag_all_sweeps['sweep_number_sub'].values[sag_currentsteps_min_idx]
                
                # + ri across all stable sweeps
                ri, r2 = self.process_inputresistance
                df['input_resistance'] = ri
                df['r2_value'] = r2
                    
                # export
                if None not in [fdir, fname, file_extension]:
                    export_df(data = self.data, df = df, fdir = fdir, fname = fname, file_extension = '.xlsx')
                    return df
                else: 
                    return df
            else: 
                raise ValueError(f'> 1 current steps found close to {i_search}'
                                 ' for subthreshold feature selection...')
        else: 
            raise TypeError('pass a current step to select sag'
                            ' values for as an int type ...')
    
        
    def df_all_sag_features(self, fdir = None, fname = None, file_extension = '.xlsx'): 
        """ return df of all sag features found per sweep """
        
        df_all_sag_features = self.process_sag
        
        # export
        if None not in [fdir, fname, file_extension]:
            export_df(data = self.data, df = df_all_sag_features,\
                        fdir = fdir, fname = fname, file_extension = '.xlsx')
        else: 
            pass
    
        return df_all_sag_features
    
    
    @property
    def _sweep_qc_sub(self): 
        """ qc on sweepdata for rms stability + depol steps """
        
        # check for depolarization steps :: remove sweeps < 0 pA stimuli 
        self.hyperpol_sweepdata, self.hyperpol_sweeptimes,\
            self.hyperpol_stimuli, self.adjusted_sweepnumbers_sub = drop_depolsweeps(self.sweepdata_sub, self.sweeptimes_sub, self.stimuli_sub)

        # remove unstable sweeps :: remove sweeps > rms cutoff 
        if self.rms_cutoff_sub is not None: 
            if len(self.hyperpol_sweepdata) > 0: 
                self.stable_sweepidx_sub, self.stable_sweepdata_sub, self.stable_sweeptimes_sub,\
                    self.stable_stimuli_sub = drop_unstablesweeps_rms(self.hyperpol_sweepdata, self.hyperpol_sweeptimes, self.hyperpol_stimuli,\
                                                                end = self.end, srate = self.srate, rms_cutoff = self.rms_cutoff_sub,\
                                                                baseline_interval = self.baseline_interval_sub)
            else: 
                self.stable_sweepidx_sub = []; self.stable_sweepdata_sub = []; self.stable_sweeptimes_sub = []; self.stable_stimuli_sub = []
        else: 
            # set >> 10 if no stability to be checked
            raise ValueError(f'remove unstable sweeps for sag calculations | pass an rms cutoff: {self.rms_cutoff_sub}') 
    
    
    def plot_ri(self, figdir = None, figname = None, figextension = None): 
        """ sanity check :: plot input resistance relationship """
        
        df_sag_all_sweeps = self.process_sag
        
        v_peak = df_sag_all_sweeps['deflect_v'].values
        i = df_sag_all_sweeps['sag_currentsteps'].values
        
        linregress_dict = measure_linregress(i = i, v = v_peak)
        
        if v_peak.size > 0: 
            ri_plot(v_peak = v_peak, i = i, figdir = figdir, figname = figname,\
                    figextension = figextension, **linregress_dict)
        else: 
            fname = self.data.metadata['abf_id']
            print(f'no voltage and i values found to plot ri for {fname} '
                  '| check qc parameters ...')

    
    def plot_sag(self, sweeps = None, deflect_v = False, show_all_stable = False, xlim = None,\
                ylim_v = [None, None], ylim_i = [None, None], scale_bar = True, axis = False,\
                figdir = None, figname = None, figextension = None):
        """ plot sag features """
        
        if sweeps is not None: 
            pass
        else: 
            sweeps = self.stable_sweepidx_sub[0] # default :: collect all stable
            
        df_sag_all_sweeps = self.process_sag
        
        # collect stable sweeps 
        if show_all_stable:
            stable_sweeps_sub = self.adjusted_sweepnumbers_sub[self.stable_sweepidx_sub[0]]
            print(f'plotting stable sweeps | {stable_sweeps_sub}')
        else: 
            stable_sweeps_sub = None 
            
        # deflect idx 
        if deflect_v:
            if sum(np.in1d(self.stable_sweepidx_sub, np.array(sweeps))) > 0: 
                
                deflect_idx = []
                for sweep in sweeps: 
                    try: 
                        deflect_idx.append(df_sag_all_sweeps.loc[sweep, 'deflect_index'])
                    except: 
                        deflect_idx.append(None)
                show_all_stable = False # default off 
            else: 
                deflect_idx = None 
        else: 
            deflect_idx = None 
        
        if len(self.sweepdata_sub) > 0: 
            sag_plot(t = self.sweeptimes_sub, i = self.stimuli_sub, v = self.sweepdata_sub, sweeps = sweeps,\
                    xlim = xlim, ylim_v = ylim_v, ylim_i = ylim_i, stable_sweeps = stable_sweeps_sub,\
                    scale_bar = scale_bar, deflect_idx = deflect_idx, axis = axis,\
                    start = self.start, end = self.end, figdir = figdir, figname = figname, figextension = figextension)
        else: 
            fname = self.data.metadata['abf_id']
            print(f'no stable sweep data to plot found for {fname} ...')
            
        
    def plot_subthreshold_allsweeps(self, show_all_stable = True, figdir = None, figname = None, figextension = None): 
            """ return plot of all sweeps """
            
            df_sag_all_sweeps = self.process_sag  
                  
            # collect stable sweeps 
            if show_all_stable:
                stable_sweeps = self.stable_sweepidx_sub[0]
                print(f'plotting stable sweeps | {self.adjusted_sweepnumbers_sub[stable_sweeps]}')
            else: 
                stable_sweeps = None 
            
            if len(self.sweepdata_sub) > 0: 
                subthreshold_plot_allsweeps(t = self.sweeptimes_sub, v = self.sweepdata_sub,\
                                        stable_sweeps = self.adjusted_sweepnumbers_sub[stable_sweeps],\
                                        start = self.start, end = self.end, srate = self.srate,\
                                        figdir = figdir, figname = figname, figextension = figextension)
            else: 
                fname = self.data.metadata['abf_id']
                print(f'no stable sweep data to plot found for {fname} ...')