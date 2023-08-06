"""
database_metadata.py

Human brain patch-clamp data metadata 
from neurophysiology archives (i.e. Allen Brain, DANDI). 

"""

from ...download.allenbrain.query import AllenBrainQuery

###################################################################################################
###################################################################################################

def database_metadata(database = 'Allen Brain', manifest_file = None, file_name = None, specimen_id = None): 
    """ return metadata dict from select databases
    
    Parameters:
    ------------
    
    file_name: string
        File name to save/read the cell metadata as JSON.  If file_name is None,
        the file_name will be pulled out of the manifest.  If caching
        is disabled, no file will be saved. Default is None.

    manifest_file: string
       File name of the manifest to be read.  Default is "cell_types_manifest.json".
    
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
                return AllenBrainQuery(file_name = file_name, manifest_file = manifest_file,\
                                            specimen_id = specimen_id).metadata_all
            else: 
                raise ValueError(f'set manifest file path: {manifest_file} ...')
    else: 
        print(f'select a database: {databases} ...')
    
    