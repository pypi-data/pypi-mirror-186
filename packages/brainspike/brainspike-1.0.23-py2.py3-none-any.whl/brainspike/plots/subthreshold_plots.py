"""
subthreshold_plots.py

Modules for plotting subthreshold
features and sweepdata. 

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

def subthreshold_plot_allsweeps(t = None, v = None, start = None, end = None, srate = None, figdir = None,\
                            figname = None, figextension = None, stable_sweeps = None): 
    """ subthreshold plot across all sweeps """
    
    plt.style.use(os.path.join(os.path.dirname(__file__),'..','utils/plots/paper.mplstyle'))
    fig, ax = plt.subplots(1,1, figsize=(6,5))

    for sweep_number in range(len(v)):
        ax.plot(t[sweep_number][int((start-0.5)*srate):int((end+0.5)*srate)] + (.25) * sweep_number,\
            v[sweep_number][int((start-0.5)*srate):int((end+0.5)*srate)] + 15 * sweep_number, color='black', lw = 1)
        
    # stable sweeps vs unstable
    if stable_sweeps is not None:       
        for stable_sweep in stable_sweeps: 
            ax.plot(t[stable_sweep][int((start-0.5)*srate):int((end+0.5)*srate)] + (.25) * stable_sweep,\
                    v[stable_sweep][int((start-0.5)*srate):int((end+0.5)*srate)] + 15 * stable_sweep, color = 'royalblue', label = 'included')
    else: 
        pass 

    ax.legend(*[*zip(*{l:h for h,l in zip(*ax.get_legend_handles_labels())}.items())][::-1],\
                bbox_to_anchor=[1.2, 0.8], loc='center')
        
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


def sag_plot(t = None, i = None, v = None, sweeps = None, xlim = None, ylim_v = None,\
            ylim_i = None, stable_sweeps = None, deflect_idx = None, scale_bar = True, axis = False,\
            start = None, end = None, figdir = None, figname = None, figextension = None): 
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
            ax[0].plot(t[sweep], v[sweep], color = 'k')
            ax[1].plot(t[sweep], i[sweep], color = 'k')
            if (deflect_idx is not None) and (deflect_idx[count] is not None): # show deflect idx 
                ax[0].scatter(t[sweep][deflect_idx[count]], v[sweep][deflect_idx[count]], s = 60, color = 'orange')
        
    # stable sweeps vs unstable
    if stable_sweeps is not None: 
        for sweep in range(len(v)): 
            ax[0].plot(t[sweep], v[sweep], color = 'tab:red', lw = 1.5)
            ax[1].plot(t[sweep], i[sweep], color = 'tab:red', lw = 1.5)
            
        for stable_sweep in stable_sweeps: 
            ax[0].plot(t[stable_sweep], v[stable_sweep], color = 'royalblue')
            ax[1].plot(t[stable_sweep], i[stable_sweep], color = 'royalblue')
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
    
    # adjusted lims 
    ymin_i, ymax_i = ax[1].get_ylim()
    ymin, ymax = ax[0].get_ylim()
    xmin, xmax = ax[0].get_xlim() 
    
    # axis labels
    ax[0].set_ylabel('Voltage (mV)')
    ax[1].set_ylabel('Current (pA)')
    ax[1].set_xlabel('Time (sec.)')
    
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
    
    # reference voltage hlines 
    if ymax > 0: 
        ax[0].axhline(y=0, color='k', linestyle='--', alpha=0.3)
        ax[0].text(xmin-0.1, 0, str(0) + ' mV', ha='center', va='center', color='darkgray')
    else: 
        pass 
    
    ax[0].axhline(y=-60, color='k', linestyle='--', alpha=0.3)
    ax[0].axhline(y=-80, color='k', linestyle='--', alpha=0.3)
    ax[0].text(xmin-0.1, -60, '-60 mV', ha='center', va='center', color='darkgray')
    ax[0].text(xmin-0.1, -80, '-80 mV', ha='center', va='center', color='darkgray') 
    
    # scale bar
    if scale_bar: 
        ax[0].vlines(x = xmax-0.1, ymin = ymax, ymax = ymax-20, color='black', lw = 1.5, transform = ax[0].transData) # 20 mV 
        ax[0].text(xmax-0.05, ymax-14, '20 mV', color='black', transform = ax[0].transData) 
        
        scalebar_t = AnchoredSizeBar(ax[0].transData, 0.250, "250 ms", 'upper right', frameon=False,\
                    size_vertical=0.5, pad=1.2, bbox_to_anchor=Bbox.from_bounds(0, 0, 0.4, 1), bbox_transform=ax[0].figure.transFigure) 
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
