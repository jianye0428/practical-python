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
    sum = 0
    for row in rows:
        sum = sum + int(row[1])*float(row[2])
    return sum
cost = portfolio_cost('/home/jianye/practical-python/Work/Data/portfolio.csv')
print("Total Cost: ",cost)