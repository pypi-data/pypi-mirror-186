"""
spiketrain_plots.py

Modules for plotting pike train features and sweepdata. 

"""

import os 

import numpy as np 

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib import style
from matplotlib.ticker import AutoMinorLocator
from matplotlib.transforms import Bbox
from matplotlib.offsetbox import AnchoredText

from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar

from ..utils.plots.save import (create_path)

###################################################################################################
###################################################################################################

def spiketrain_plot_allsweeps(t = None, v = None, start = None, end = None, srate = None, figdir = None,\
                            figname = None, figextension = None, stable_sweeps = None): 
    """ spiketrain plot across all sweeps """
    
    plt.style.use(os.path.join(os.path.dirname(__file__),'..','utils/plots/paper.mplstyle'))
    fig, ax = plt.subplots(1,1, figsize=(6,5))

    for sweep_number in range(len(v)):
        ax.plot(t[sweep_number][int((start-0.5)*srate):int((end+0.5)*srate)] + (.25) * sweep_number,\
            v[sweep_number][int((start-0.5)*srate):int((end+0.5)*srate)] + 15 * sweep_number, color='black', lw = 1.5)
        
    # stable sweeps vs unstable
    if stable_sweeps is not None:       
        for stable_sweep in stable_sweeps: 
            ax.plot(t[stable_sweep][int((start-0.5)*srate):int((end+0.5)*srate)] + (.25) * stable_sweep,\
                    v[stable_sweep][int((start-0.5)*srate):int((end+0.5)*srate)] + 15 * stable_sweep, color = 'royalblue', label = 'included')
        
    else: 
        pass 

    ax.legend(*[*zip(*{l:h for h,l in zip(*ax.get_legend_handles_labels())}.items())][::-1],\
                bbox_to_anchor=[1.2, 0.7], loc='center')
        
    plt.gca().axis('off') 
    
    # save 
    #------
    if None not in [figdir, figname, figextension]: 
        if (figextension == '.png') | (figextension == '.pdf'):
            fname = create_path(figdir, figname, figextension)
            print(f"saving plt to {fname} ...")
            plt.savefig(fname, dpi = 300, bbox_inches="tight")   
            plt.show()
        else: 
            raise TypeError('file extension option are only .pdf or .png ...')
    else: 
        plt.show()
        
    
def spiketrain_plot(t = None, i = None, v = None, sweeps = None, xlim = None, ylim_v = None,\
            ylim_i = None, stable_sweeps = None, scale_bar = True, axis = False, start = 0, end = 2.5,\
            features_info = None, min_peak = 0, figdir = None,\
            figname = None, figextension = None): 
    """ plot sag features for selected sweeps """
    
    if (sweeps, list): 
        pass
    else: 
        raise TypeError('pass sweep values as a list ...')
    
    plt.style.use(os.path.join(os.path.dirname(__file__),'..','utils/plots/paper.mplstyle'))
    fig, ax = plt.subplots(2,1, figsize=(6,5), gridspec_kw={'height_ratios': [4, 1]}, sharex = True)
    
    # selected sweeps 
    if sweeps is not None:        
        for count, sweep in enumerate(sweeps): 
            ax[0].plot(t[sweep], v[sweep], color = 'k', lw = 1.5)
            ax[1].plot(t[sweep], i[sweep], color = 'k', lw = 1.5)

            if (features_info is not None): # + features 
                for feature_sweep, feature_idx, feature_color, feature_label in zip(features_info[:,0],\
                                                                                    features_info[:,1],\
                                                                                    features_info[:,2],\
                                                                                    features_info[:,3]): 
                    if sweep == int(feature_sweep):
                        ax[0].scatter(t[sweep][int(float(feature_idx))], v[sweep][int(float(feature_idx))], s=70, alpha=0.4,\
                                        color = feature_color, label = feature_label[:-6])
                    else: 
                        pass 
            else: 
                pass 

    # stable sweeps vs unstable
    if stable_sweeps is not None: 
        for sweep in range(len(v)): 
            ax[0].plot(t[sweep], v[sweep], color = 'tab:red', lw = 1.5)
            ax[1].plot(t[sweep], i[sweep], color = 'tab:red', lw = 1.5)
            
        for stable_sweep in stable_sweeps: 
            ax[0].plot(t[stable_sweep], v[stable_sweep], color = 'royalblue', lw = 1.5)
            ax[1].plot(t[stable_sweep], i[stable_sweep], color = 'royalblue', lw = 1.5)
    else: 
        pass 
    
    # default xlim  +/- 200 ms around
    # stimuli start and end 
    if xlim is None: 
        xlim = [start - 0.2, end + 0.2] 
    else: 
        pass 
    
    # lims 
    ax[1].set_xlim(xlim)
    ax[0].set_ylim(ylim_v)
    ax[1].set_ylim(ylim_i)
    
    # readjusted lims
    xmin, xmax = ax[0].get_xlim() 
    
    # threshold lims 
    ax[0].axhline(y=min_peak, color='k', linestyle='--', alpha=0.3)
    ax[0].axhline(y=-60, color='k', linestyle='--', alpha=0.3)
    
    ax[0].text(xmin-0.1,  min_peak, str(int(min_peak)) + ' mV', ha='center', va='center', color='darkgray')
    ax[0].text(xmin-0.1, -60, '-60 mV', ha='center', va='center', color='darkgray')
    
    # legend for feature info 
    if features_info is not None: 
        ax[0].legend(*[*zip(*{l:h for h,l in zip(*ax[0].get_legend_handles_labels())}.items())][::-1],\
                    bbox_to_anchor=[1.2, 0.7], loc='center')
            
    # axis labels
    ax[0].set_ylabel('v (mV)')
    ax[1].set_ylabel('Current (pA)')
    ax[1].set_xlabel('t (sec.)')
    
    # axes
    if axis is False: 
        ax[0].axis('off')
        ax[1].axis('off')
    else: 
        pass 
    
    # current step + label 
    i_min = np.min(np.array(i).take(sweeps, axis = 0))
    i_max = np.max(np.array(i).take(sweeps, axis = 0))
    
    if (i_min == 0) and (i_max > 0): # repos label to top or bottom of the step 
        currentstep = i_max 
        ylim_pos = i_max + i_max*0.3
        va = 'top'
    elif (i_min < 0) and (i_max == 0): 
        currentstep = i_min 
        ylim_pos = i_min - abs(i_min*0.3)
        va = 'bottom'
    elif (i_min < 0) and (i_max > 0): 
        currentstep = i_min 
        ylim_pos = i_min - abs(i_min*0.3)
        va = 'bottom'
    else: 
        currentstep = 0
        ylim_pos = -20
        va = 'bottom'
        
    label = str(currentstep) + ' pA'
    ax[1].text(((start + (end - start)/2)), ylim_pos, label, color='k', ha='center', va=va, transform=ax[1].transData) 
    
    # scale bar
    if scale_bar:
        scalebar_t = AnchoredSizeBar(ax[0].transData, 0.2, "200 ms", 'upper right', frameon=False,\
                    size_vertical=0.5, pad=1, bbox_to_anchor=Bbox.from_bounds(0, 0, 1, 1), bbox_transform=ax[0].figure.transFigure) 
        ax[0].add_artist(scalebar_t)
    else: 
        pass 

    plt.subplots_adjust(wspace=0, hspace=0) # reduce subplot gaps
    
    # save 
    #------
    if None not in [figdir, figname, figextension]: 
        if (figextension == '.png') | (figextension == '.pdf'):
            fname = create_path(figdir, figname, figextension)
            print(f"saving plt to {fname} ...")
            plt.savefig(fname, dpi = 300, bbox_inches="tight")   
            plt.show()
        else: 
            raise TypeError('file extension option are only .pdf or .png ...')
    else: 
        plt.show()
        
        
def i_f_plot(i = None, f = None, rheobase = None, max_firing = None, figdir = None,\
            figname = None, figextension = None): 
    """ current vs frequency relationship plot w/ rheobase & max firing sweep """
    
    plt.style.use(os.path.join(os.path.dirname(__file__),'..','utils/plots/paper.mplstyle'))
    fig, ax = plt.subplots(1,1, figsize=(6,5))
    
    # i vs f 
    ax.plot(i,f, lw = 2., color = 'black', alpha = 1)
    
    # + rheobase 
    rheobase_idx = np.where(i == rheobase)
    ax.scatter(i[rheobase_idx[0]], f[rheobase_idx[0]], s=120, facecolors='none', edgecolors='tab:red', label = 'rheobase')
    
    # + max firing sweep 
    max_firing_idx = np.where(f == max_firing)
    if max_firing_idx[0].size > 1: 
        max_firing_idx = max_firing_idx[0][0] # firing rate the same :: default to 1st index
    else: 
        max_firing_idx = max_firing_idx[0]
        
    ax.scatter(i[max_firing_idx], f[max_firing_idx], s=120, facecolors='none', edgecolors='royalblue', label = 'max firing')
    
    # legend
    ax.legend(bbox_to_anchor=[1.2, 0.7], loc='center')

    # axis labels
    ax.set_ylabel('Firing frequency (Hz)')
    ax.set_xlabel('Current (pA)')
    
    # minor tick adjustments
    y_minor_locator = AutoMinorLocator(5)
    x_minor_locator = AutoMinorLocator(5)
    ax.xaxis.set_minor_locator(x_minor_locator)
    ax.yaxis.set_minor_locator(y_minor_locator)
    
    # save 
    #------
    if None not in [figdir, figname, figextension]: 
        if (figextension == '.png') | (figextension == '.pdf'):
            fname = create_path(figdir, figname, figextension)
            print(f"saving plt to {fname} ...")
            plt.savefig(fname, dpi = 300, bbox_inches="tight")   
            plt.show()
        else: 
            raise TypeError('file extension option are only .pdf or .png ...')
    else: 
        plt.show()