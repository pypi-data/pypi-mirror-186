"""
spike_plots.py

Modules for plotting spike and 
spike train features and sweepdata. 

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

def spike_plot(t = None, i = None, v = None, peak_index = None, sweep = None, slice_window = None,\
                srate = None, axis = False, min_peak = None, scale_bar = True, ylim_v = [None, None],\
                ylim_phase = [None, None], xlim_phase = [None, None], figdir = None, figname = None, figextension = None): 
    """ plot phase plot and isolated spike event within a window """
    
    if (sweep, int): 
        pass
    else: 
        raise TypeError('pass sweep values as a list ...')
    
    plt.style.use(os.path.join(os.path.dirname(__file__),'..','utils/plots/paper.mplstyle'))
    fig, ax = plt.subplots(1,2, figsize=(6,3))
    
    # selected sweeps 
    if sweep is not None:     
        
        # isolated spike plot 
        v_slice = v[sweep][peak_index+int(slice_window[0]*srate):peak_index+int(slice_window[1]*srate)] # slice v and t arr
        t_slice = t[sweep][peak_index+int(slice_window[0]*srate):peak_index+int(slice_window[1]*srate)]  
        ax[0].plot(t_slice, v_slice, color = 'k')
        
        # phase plot  
        peakv_deriv = np.diff(v_slice) * (srate/1000) # scale to v/s (mV/ms) 
        ax[1].plot(v_slice[1:], peakv_deriv, color = 'k', lw = 2)
        
    # lims 
    ax[0].set_ylim(ylim_v)
    ax[1].set_ylim(ylim_phase)
    ax[1].set_xlim(xlim_phase)
    
    # axis labels
    ax[0].set_ylabel('Voltage (mV)')
    ax[0].set_xlabel('Time (sec.)')
    
    # axes
    if axis is False: 
        ax[0].axis('off')
    else: 
        pass 
    
    # threshold lims 
    ymin, ymax = ax[0].get_ylim(); xmin, xmax = ax[0].get_xlim() 
    ax[0].axhline(y=min_peak, color='k', linestyle='--', alpha=0.3)
    ax[0].axhline(y=-60, color='k', linestyle='--', alpha=0.3)
    
    ax[0].text(xmin-0.2, min_peak, str(int(min_peak)) + ' mV', ha='center', va='center', color='darkgray')
    ax[0].text(xmin-0.2, -60, '-60 mV', ha='center', va='center', color='darkgray')
    
    # scale bar
    if scale_bar:
        scalebar_t = AnchoredSizeBar(ax[0].transData, 0.002, "2 ms", 'upper right', frameon=False,\
                    size_vertical=0.5, pad=1.2, bbox_to_anchor=Bbox.from_bounds(0, 0, 0.5, 1), bbox_transform=ax[0].figure.transFigure) 
        ax[0].add_artist(scalebar_t)
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

