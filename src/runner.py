import sys
import AnalyticsEngine as  processing_engine
import DataTransformer as transformer
from H1BDataFrame import DataFrame

def run(input_file, occupation_stat_file, state_stat_file):
    raw_data = DataFrame.read_csv(input_file)
    data = transformer.standardize_col_names(raw_data)
    occupation_stats = processing_engine.get_occupation_stats(data)
    state_stats = processing_engine.get_state_stats(data)
    occupation_stats.to_csv(occupation_stat_file)
    state_stats.to_csv(state_stat_file)


run(sys.argv[1], sys.argv[2], sys.argv[3])
