def write(results, file_name, delimiter=';'):
    with open(file_name,'w') as output:
        results.to_csv(output, sep=delimiter, index=False)
