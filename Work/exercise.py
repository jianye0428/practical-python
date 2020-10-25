
# for i in range(10):
#     print("i=",i)

# for n in range(0,10,1):
#     print(n,end=' ')

# for i in range(0,10,2):
#     print(i, end=' ')

# data = [4,9,1,25,16,100,49] #list
# print(type(data))
# print(min(data))

# for i in data:
#     print(i,end=' ')

# for n,x in enumerate(data):
#     print(n,x)

import os
path = os.getcwd()
import csv
import sys

# f = open('/home/jianye/practical-python/Work/Data/portfolio.csv')
# rows = csv.reader(f)
# headers = next(rows)
# sum = 0
# for rowno, row in enumerate(rows,start = 1):
#     try:
#         sum = sum + int(row[1])*float(row[2])
#     except ValueError:
#         print(f'Row {rowno}: Bad Row: {row}')

# f=open('/home/jianye/practical-python/Work/Data/portfolio.csv')
# rows = csv.reader(f)
# headers = next(rows)
# print(headers)
# row = next(rows)
# print(row)
# print(list(zip(headers,row)))#list
# print(dict(zip(headers,row)))#dict

portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]

from collections import Counter

total_shares = Counter()

for name, shares, price in portfolio:
    total_shares[name] += shares
# print(total_shares['IBM'])#150


# one-many mapping
from collections import defaultdict

holdings = defaultdict(list)

for name,shares,price in portfolio:
    holdings[name].append((shares,price))
# print(holdings['IBM'])

from collections import deque
# history = deque(maxlen=N)
# with open(filename) as f:
#     for line in f:
#         history.append(line)
#         ...


#List Comprehension
#1
# a = [1,2,3,4,5]
# b = [2*x for x in a]
# print(b)

#2
# names = ['Elwood','Jake']
# a = [name.lower() for name in names]
# print(a)

#3 Filtering
# a = [1,-5,4,2,-2,10]
# b = [2*x for x in a if x > 0]
# print(b) 