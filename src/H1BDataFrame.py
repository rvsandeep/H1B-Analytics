import csv
HEAD = 5

class DataFrame:

    def __init__(self, data, columns=None, sep=';', header=True):
        self.sep = sep
        self.header = header
        self.data = data
        self.columns = None
        if header:
            self.set_header(columns)

    # class method to read a csv file and return a dataframe
    @classmethod
    def read_csv(cls, input_file, sep=';', header=True):
        data = []
        with open(input_file, 'r') as fp:
            for row in csv.reader(fp, delimiter=sep, skipinitialspace=True):
                data.append(row)
        if (header) :
            columns = data.pop(0)
        return cls(data, columns=columns)

    #write the data to a csv file
    def to_csv(self, output_file):
        with open(output_file, 'w') as fp:
            datawriter = csv.writer(fp, delimiter=self.sep)
            if self.header :
                datawriter.writerow(list(self.columns.keys()))
            for row in self.data:
                datawriter.writerow(row)

    #updated the header of the dataframe
    def set_header(self, columns):
        if columns is None:
            return None

        # using an existing name -> col_index mapping
        if type(columns) is dict:
            self.columns = columns
            return None

        # converting a list to name -> col_index mapping for quicker  access of feature position
        if type(columns) is list:
            self.columns = {}
            for idx, item in enumerate(columns):
                self.columns[item] = idx
        return None

    #return the header of the dataframe in order
    def get_header(self):
        if self.header is False:
            return None
        return sorted(self.columns, key=lambda k: self.columns[k])

    #renaming column names
    def rename_columns(self, columns = None, inplace=False):
        if inplace :
            new_frame = self
        else :
            new_frame = DataFrame(self.data, self.columns)

        for current_name in columns.keys():
            idx = new_frame.columns.pop(current_name, None)
            if idx is not None:
                new_name = columns[current_name]
                new_frame.columns[new_name] = idx

        return new_frame

    #filter rows based on a feature value
    def filter(self, colname, colvalue):
        cidx = self.columns.get(colname, None)
        if cidx is None:
            print('No Such Column Error')
        result = []
        for ridx, row in enumerate(self.data):
            if row[cidx] == colvalue:
                result.append(ridx)
        return DataFrame([self.data[idx] for idx in result], self.columns)

    #return the unique values in a feature 
    def unique_column_values(self, colname, return_counts=False, ignore_na = False):
        cidx = self.columns.get(colname, None)
        if cidx is None:
            print('No Such Column Error')
        col_values = [ row[cidx] for row in self.data]
        if (return_counts == False):
            return list(set(col_values))
        freq = {}
        for val in col_values:
            if ignore_na and len(val) == 0:
                continue
            count = freq.get(val, 0)
            count += 1
            freq[val] = count
        return (list(freq.keys()), list(freq.values()))

    def __str__(self):
        columns = self.get_header()
        res = [columns]
        res.extend(self.data[:HEAD])
        return str(res)
