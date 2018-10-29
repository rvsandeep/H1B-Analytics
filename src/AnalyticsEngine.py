import numpy as np
import pandas as pd

def top10_features(feature):
    feature, counts = np.unique(feature, return_counts=True)
    indices = [x for _,x in sorted(
        zip(counts,list(range(0, len(counts))) ), reverse=True ) ]
    return feature[indices], counts[indices]

def top10_stats(feature):
    features, counts = top10_features(feature)
    percents = 100 * (counts / np.sum(counts))
    precents = np.core.defchararray.add(percents.astype('str'), ['%']*len(percents) )
    return [[ features[i] , counts[i], percents[i]] for i in range(0, len(counts))]

def get_occupation_stats(data):
    results = top10_stats(data.occupation)
    col_names = ['TOP_OCCUPATION','NUMBER_CERTIFIED_APPLICATIONS','PERCENTAGE' ]
    return pd.DataFrame(results, columns= col_names)

def get_state_stats(data):
    results = top10_stats(data.worksite_state)
    col_names = ['TOP_STATES','NUMBER_CERTIFIED_APPLICATIONS','PERCENTAGE' ]
    return pd.DataFrame(results, columns= col_names)
