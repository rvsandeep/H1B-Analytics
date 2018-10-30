from operator import itemgetter
from H1BDataFrame import DataFrame

def top_values(H1BData, feature):
    feature, counts = H1BData.unique_column_values(feature, return_counts=True, ignore_na=True)
    sorted_ = sorted( zip(feature,counts), key=lambda val:(-val[1], val[0]))
    unzipped_ = list(zip(*sorted_))
    return list(unzipped_[0]), list(unzipped_[1])

def topk_stats(H1BData, feature, k=10):
    features, counts = top_values(H1BData, feature)
    total = sum(counts)
    # percentage calculationf for the top k values
    percent_conversion = [100.0 / total] * k
    percents = [str(round(a*b, 1)) +'%' for a,b in zip(counts, percent_conversion)]
    return [[ features[i] , counts[i], percents[i]] for i in range(0, min(k, len(counts))) ]

def get_occupation_stats(H1BData):
    certified_applications = H1BData.filter('CASE_STATUS', "CERTIFIED")
    results = topk_stats(certified_applications, 'SOC_NAME')
    col_names = ['TOP_OCCUPATIONS','NUMBER_CERTIFIED_APPLICATIONS','PERCENTAGE' ]
    return DataFrame(results, columns= col_names)

def get_state_stats(H1BData):
    certified_applications = H1BData.filter('CASE_STATUS', "CERTIFIED")
    results = topk_stats(certified_applications, 'WORKSITE_STATE')
    col_names = ['TOP_STATES','NUMBER_CERTIFIED_APPLICATIONS','PERCENTAGE' ]
    return DataFrame(results, columns= col_names)
