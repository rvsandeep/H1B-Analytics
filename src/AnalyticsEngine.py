from operator import itemgetter
from H1BDataFrame import DataFrame

def top10_values(H1BData, feature):
    feature, counts = H1BData.unique_column_values(feature, return_counts=True)
    sorted_ = sorted( zip(feature,counts), key=lambda val:(-val[1], val[0]))
    unzipped_ = list(zip(*sorted_))
    return list(unzipped_[0]), list(unzipped_[1])

def top10_stats(H1BData, feature):
    features, counts = top10_values(H1BData, feature)
    percent_conversion = [100.0 / sum(counts)] * len(counts)
    percents = [str(a*b)+'%' for a,b in zip(counts, percent_conversion)]
    return [[ features[i] , counts[i], percents[i]] for i in range(0, len(counts))]

def get_occupation_stats(H1BData):
    certified_applications = H1BData.filter('CASE_STATUS', "CERTIFIED")
    results = top10_stats(certified_applications, 'SOC_NAME')
    col_names = ['TOP_OCCUPATIONS','NUMBER_CERTIFIED_APPLICATIONS','PERCENTAGE' ]
    return DataFrame(results, columns= col_names)

def get_state_stats(H1BData):
    certified_applications = H1BData.filter('CASE_STATUS', "CERTIFIED")
    results = top10_stats(certified_applications, 'WORKSITE_STATE')
    col_names = ['TOP_STATES','NUMBER_CERTIFIED_APPLICATIONS','PERCENTAGE' ]
    return DataFrame(results, columns= col_names)
