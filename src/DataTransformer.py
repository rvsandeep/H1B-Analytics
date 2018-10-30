import json
import os
RESOURCE_DIR = 'src/resources/'

def standardize_col_names(raw_data):
    fileformats = os.listdir(RESOURCE_DIR)
    standard_mapping = {}
    for fileformat in fileformats:
        new_mapping = json.loads(open(RESOURCE_DIR+fileformat).read())
        standard_mapping = {**standard_mapping, **new_mapping}
    return raw_data.rename_columns(columns = standard_mapping)
