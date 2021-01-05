import os

# print(os.getcwd())
# with open('Work/Data/portfolio.csv','rt') as f:
#     data = f.read()

# print(data)


# with open('Work/Data/portfolio.csv','rt') as f:
#     for line in f:
#         print(line)


# with open('Work/Data/portfolio.csv','rt') as f:
#     header = next(f)
#     for line in f:
#         print(line)
sum=0
with open('Work/Data/portfolio.csv','rt') as f:
    header = next(f).split(',')
    for line in f:
        row = line.split(',')
        sum = sum+int(row[1])*float(row[2])
        #print(row)
print("Total cost ", sum)