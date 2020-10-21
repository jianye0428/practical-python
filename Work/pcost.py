# pcost.py
#
# Exercise 1.27

import os
os.getcwd()
# with open('/home/jianye/practical-python/Work/Data/portfolio.csv','rt') as f:
#     data = f.read()
# print(data)

lists=[]
with open('/home/jianye/practical-python/Work/Data/portfolio.csv','rt') as f:
    headers = next(f)
    for line in f:   
        lists.append(line.split(',')) 
        print(line.split(','))

print(lists)
sum = 0
for list in lists:
    sum= sum+ int(list[1])*float(list[2])
print(sum)