import pandas as pd

def read(input_file, delimiter=";"):
    raw_data = pd.read_csv(input_file, header=0, sep=delimiter, index_col=0)
    return raw_data
