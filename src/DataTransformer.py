
COL_NAME_MAPPING = {'CASE_STATUS' : 'status'}

def standardize_col_names(raw_data):
    return raw_data.rename(columns = COL_NAME_MAPPING)
