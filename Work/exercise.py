
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

f=open('/home/jianye/practical-python/Work/Data/portfolio.csv')
rows = csv.reader(f)
headers = next(rows)
print(headers)
row = next(rows)
print(row)
print(list(zip(headers,row)))#list
print(dict(zip(headers,row)))#dict