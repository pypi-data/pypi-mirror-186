"""
dataframes.py

Modules for exporter utilities. 

"""

import os
import json 

import numpy as np

import pandas as pd

from ..utils.plots.save import (create_path)

###################################################################################################
###################################################################################################


def export_df(data = None, df = None, fdir = None, fname = None, file_extension = '.xlsx'): 
    """ export df w/ metadata and preprocessing parameters attached """

    if df is not None: 
        
        if None not in [fdir, fname, file_extension]:
            if file_extension == '.xlsx': 
                fname = create_path(fdir, fname, file_extension)
                # print(f"saving df to {fname} ...")
                
                try: 
                    np.set_printoptions(threshold=np.nan) # stop truncating the output strings
                except ValueError: # https://github.com/numpy/numpy/issues/12987
                    pass
                
                df.to_excel(fname)   
                
            else: 
                print(f'unable to export {file_extension} formats ...')
        else: 
            pass 
    else: 
        raise TypeError('pass df for exporting ...')
    