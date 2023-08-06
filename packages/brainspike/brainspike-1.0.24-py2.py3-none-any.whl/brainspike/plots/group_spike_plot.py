"""
spiketrain_plots.py

Modules for plotting pike train features and sweepdata. 

"""

import os 

import numpy as np 

import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.ticker import AutoMinorLocator
from matplotlib.transforms import Bbox

from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar

from ..plots.plot_utils import (smooth_data)

from ..utils.plots.save import (create_path)

###################################################################################################
###################################################################################################

def group_i_f_plot(i = None, f = None, sem = None, smooth_window = None, figname = None,\
                   figdir = None, figextension = None): 
    """ plot i vs f relationship for group data w/ sem error bars """

    plt.style.use(os.path.join(os.path.dirname(__file__),'..','utils/plots/paper.mplstyle'))
    fig, ax = plt.subplots(1,1, figsize=(6,5))
    
    if smooth_window is not None: # smooth window
        i = smooth_data(i, smooth_window)
        f = smooth_data(f, smooth_window)
        sem = smooth_data(sem, smooth_window)
    else: 
        pass 
    
    ax.plot(i, f, lw = 2., color = 'royalblue')
    ax.fill_between(i, f-sem, f+sem, alpha = 0.2, color = 'royalblue', edgecolor = 'w')

    # labels
    ax.set_xlabel('Current (pA)')
    ax.set_ylabel('Firing frequency (Hz)')

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
        
        
def group_spike_plot(t = None, v = None, peak_v_deriv = None, sem_v = None, sem_v_deriv = None,\
                        min_peak = None, scale_bar = None, axis = None, figdir = None, figname = None, figextension = None,\
                        ylim_v = [None, None], ylim_phase = [None, None], xlim_phase = [None, None]): 
    """ plot spike for group data w/ sem error bars """
    
    plt.style.use(os.path.join(os.path.dirname(__file__),'..','utils/plots/paper.mplstyle'))
    fig, ax = plt.subplots(1,2, figsize=(6,3))
    
    ax[0].plot(t, v, lw = 2., color = 'royalblue')
    ax[0].fill_between(t, v-sem_v, v+sem_v, alpha = 0.2, color = 'royalblue', edgecolor = 'w')
    
    ax[1].plot(v[1:], peak_v_deriv, lw = 2., color = 'royalblue')
    ax[1].fill_between(v[1:], peak_v_deriv-sem_v_deriv, peak_v_deriv+sem_v_deriv, alpha = 0.2, color = 'royalblue', edgecolor = 'w')
    
    # axis labels
    ax[0].set_ylabel('Voltage (mV)')
    ax[0].set_xlabel('Time (sec.)')
    
    # lims 
    ax[0].set_ylim(ylim_v)
    ax[1].set_ylim(ylim_phase)
    ax[1].set_xlim(xlim_phase)
    
    # threshold lims 
    ymin, ymax = ax[0].get_ylim(); xmin, xmax = ax[0].get_xlim();
    ax[0].axhline(y=min_peak, color='k', linestyle='--', alpha=0.3)
    ax[0].axhline(y=-60, color='k', linestyle='--', alpha=0.3)
    ax[0].text(0, abs(ymin-(min_peak))/(ymax-ymin)-0.039, str(int(min_peak)) + ' mV',\
                    verticalalignment='bottom', horizontalalignment='right', transform=ax[0].transAxes, color='darkgray')
    ax[0].text(0, abs(ymin-(-60))/(ymax-ymin)-0.0375, '-60 mV', verticalalignment='bottom',\
                    horizontalalignment='right', transform=ax[0].transAxes, color='darkgray')
    
    # scale bar
    if scale_bar:
        scalebar_t = AnchoredSizeBar(ax[0].transData, 0.002, "2 ms", 'upper right', frameon=False,\
                    size_vertical=0.5, pad=1.2, bbox_to_anchor=Bbox.from_bounds(0, 0, 0.5, 1), bbox_transform=ax[0].figure.transFigure) 
        ax[0].add_artist(scalebar_t)
    else: 
        pass 
    
    # axes
    if axis is False: 
        ax[0].axis('off')
    else: 
        pass 
    
    # move left y-axis and bottom x-axis to centre,
    # passing through (0,0) for phase plot
    ax[1].spines['left'].set_position('center')
    ax[1].spines['bottom'].set_position('center')
    
    # show ticks in the left and lower axes
    # only for phase plot 
    ymin, ymax = ax[1].get_ylim(); xmin, xmax = ax[1].get_xlim() 
    ax[1].xaxis.set_ticks_position('bottom')
    ax[1].yaxis.set_ticks_position('left')
    ax[1].set_xticks([xmin, xmax]) # removing tick labels
    ax[1].set_yticks([ymin, ymax])
    
    # phaseplot txt
    ax[1].text(xmax + 50, ((ymin+ymax)/2), 'Membrane \n potential (mV)' , ha='center', va='center', transform=ax[1].transData) 
    ax[1].text(((xmin+xmax)/2), ymin-70, 'Δ Membrane \n potential (mV/ms)' , ha='center', va='center', transform=ax[1].transData) 

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