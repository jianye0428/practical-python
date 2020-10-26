import copy
a = [2,3,[100,101],4]
b = copy.deepcopy(a)
# print(a[2] is b[2])
# print(id(a))
# print(id(b))

# if isinstance(a,list):
#     print('a is not a list')


import math
items = [abs,math,ValueError]
print(items[0](-45))

# try:
#     x=int('not a number')
# except items[2]:
#     print('Failed!')


import csv
types=[str,int,float]
f = open('/home/jianye/practical-python/Work/Data/portfolio.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
# print(row)
r= list(zip(types,row))

# converted =[]
# for func, val in zip(types,row):
#     converted.append(func(val))
# print(converted)
converted = [func(val) for func, val in zip(types,row)]
# print(converted)

# print(dict(zip(headers,converted)))
# print({name:func(val) for name,func,val in zip(headers,types,row)})

f = open('/home/jianye/practical-python/Work/Data/dowstocks.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
print(headers)
print(row)
types = [str,float,str,str,float,float,float,float,int]
converted =[func(val) for func,val in zip(types,row)]
print(converted)
record = dict(zip(headers,converted))
print(record)