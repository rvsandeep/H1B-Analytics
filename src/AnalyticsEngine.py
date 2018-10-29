import numpy as np
import pandas as pd
from operator import itemgetter

def top10_features(feature):
    feature, counts = np.unique(feature, return_counts=True)
    sorted_ = sorted( zip(feature,counts), key=itemgetter(1), reverse=True)
    unzipped_ = list(zip(*sorted_))
    return list(unzipped_[0]), list(unzipped_[1])

def top10_stats(feature):
    features, counts = top10_features(feature)
    percents = 100 * (counts / np.sum(counts))
    percents = np.core.defchararray.add(percents.astype('str'), ['%']*len(percents) )
    return [[ features[i] , counts[i], percents[i]] for i in range(0, len(counts))]

def get_occupation_stats(data):
    certified_applications = data[data['CASE_STATUS'] == "CERTIFIED"]
    results = top10_stats(certified_applications.SOC_NAME)
    col_names = ['TOP_OCCUPATIONS','NUMBER_CERTIFIED_APPLICATIONS','PERCENTAGE' ]
    return pd.DataFrame(results, columns= col_names)

def get_state_stats(data):
    certified_applications = data[data['CASE_STATUS'] == "CERTIFIED"]
    results = top10_stats(certified_applications.WORKSITE_STATE)
    col_names = ['TOP_STATES','NUMBER_CERTIFIED_APPLICATIONS','PERCENTAGE' ]
    return pd.DataFrame(results, columns= col_names)
