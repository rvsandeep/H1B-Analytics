import sys
import AnalyticsEngine as  processing_engine
import DataTransformer as transformer
import Reader as reader
import Writer as writer

def run(input_file, occupation_stat_file, state_stat_file):
    raw_data = reader.read(input_file)
    data = transformer.standardize_col_names(raw_data)
    occupation_stats = processing_engine.get_occupation_stats(data)
    state_stats = processing_engine.get_state_stats(data)
    writer.write(occupation_stats, occupation_stat_file)
    writer.write(state_stats, state_stat_file)


run(sys.argv[1], sys.argv[2], sys.argv[3])
