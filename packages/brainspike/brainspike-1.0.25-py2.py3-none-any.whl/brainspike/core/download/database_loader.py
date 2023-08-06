"""
database_loader.py

Human brain patch-clamp data loader 
for neurophysiology archives (i.e. Allen Brain, DANDI). 

"""


import pandas as pd 

from ...download.allenbrain.allenbrain_obj import AllenBrain

###################################################################################################
###################################################################################################


def database_load(database = 'Allen Brain', specimen_id = None, manifest_file = None, stimulus_type = 'Long Square'): 
    """ return metadata dict from select databases
    
    
    Arugments
    ----------
    
    manifest_file: str
        path to manifest file (.json) for 
        data load. Default is "cell_types_manifest.json".
    
    Database info: 
    --------------
    
    'Allen Brain': https://celltypes.brain-map.org/
    'DANDI': https://dandiarchive.org/ 
    
    Code info:
    -----------
    
    https://github.com/AllenInstitute/AllenSDK/blob/master/allensdk/core/cell_types_cache.py 
    
    """
    
    databases = ['Allen Brain']
    # dandi_numbers = [] 
    
    if database in databases: 
        if database == 'Allen Brain': 
            if manifest_file is not None: 
                
                allenbrain_objects = []
                if isinstance(specimen_id, int): 
                    return allenbrain_objects.append(AllenBrain(specimen_id = specimen_id,\
                                                            manifest_file = manifest_file,\
                                                            stimulus_type = stimulus_type))
                
                elif isinstance(specimen_id, pd.DataFrame): 
                    try:  
                        specimen_ids = specimen_id.id.values
                        
                        for id in specimen_ids: 
                            allenbrain_objects.append(AllenBrain(specimen_id = id,\
                                                                    manifest_file = manifest_file,\
                                                                    stimulus_type = stimulus_type))
                        else: 
                            pass 
                        
                        return allenbrain_objects
                    
                    except: 
                        raise TypeError('no specimen ids found in parsed df for load ...')
            else: 
                raise ValueError(f'set manifest file path: {manifest_file} ...')
    else: 
        print(f'select a database: {databases} ...')