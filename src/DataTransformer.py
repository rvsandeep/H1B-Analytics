import json
import os
RESOURCE_DIR = 'src/resources/'

#update old column names to a new convention
def standardize_col_names(raw_data):
    fileformats = os.listdir(RESOURCE_DIR)
    standard_mapping = {}
    for fileformat in fileformats:
        new_mapping = json.loads(open(RESOURCE_DIR+fileformat).read())
        #use the latest mapping
        standard_mapping = {**standard_mapping, **new_mapping}
    return raw_data.rename_columns(columns = standard_mapping)
