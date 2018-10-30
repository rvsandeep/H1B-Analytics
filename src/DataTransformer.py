
COL_NAME_MAPPING = {'STATUS' : 'CASE_STATUS',
                    'LCA_CASE_WORKLOC1_STATE' : 'WORKSITE_STATE',
                    'LCA_CASE_SOC_NAME' : 'SOC_NAME'}

def standardize_col_names(raw_data):
    return raw_data.rename_columns(columns = COL_NAME_MAPPING)
