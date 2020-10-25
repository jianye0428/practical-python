# pcost.py
#
# Exercise 1.27

import os
os.getcwd()
import csv

def portfolio_cost(filename):
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    total_cost = 0
    for rowno, row in enumerate(rows,start = 1):
        record = dict(zip(headers,row))
        try:
            nshares = int(record['shares'])
            price = float(record['price'])
            total_cost += nshares * price
        except ValueError:
            print(f'Row {rowno}: Bad Row: {row}')
    return total_cost
# cost = portfolio_cost('/home/jianye/practical-python/Work/Data/portfolio.csv')
# print("Total Cost: ",cost)

cost = portfolio_cost('/home/jianye/practical-python/Work/Data/portfoliodate.csv')
print("Total Cost: ",cost)