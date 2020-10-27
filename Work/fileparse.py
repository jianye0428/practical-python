# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename,select=None,types=None,has_headers=False,delimiter=' ',silence_errors = True):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f,delimiter=delimiter)
        # Read the file headers
        if has_headers:
            headers = next(rows)
        else:
            raise RuntimeError("Select argument requires colums headers")
        if select:
            indices = [headers.index(colname) for colname in select]
            headers  = select
        else:
            indices = []
        records = []
        for row in rows:
            if not row:
                continue
            if indices:
                row = [row[index] for index in indices]
            if types:
                try:
                    row = [func(val) for func, val in zip(types,row)]
                except ValueError as e:
                    if not silence_errors:
                        print(f'Could\'t convert', row)
                    continue
            record = dict(zip(headers,row))
            records.append(record)
    return records


portfolio = parse_csv('/home/jianye/practical-python/Work/Data/missing.csv',select=['name','shares','price'],types=[str,int,float],has_headers=True,delimiter=',',silence_errors=True)
print(portfolio)