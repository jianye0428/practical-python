# import pcost

# a=pcost.portfolio_cost('Work/Data/portfolio.csv')
# print(a)
import follow
def filematch(filename, substr):
    for line in lines:
        if substr in line:
            yield line

# for line in open('Work/Data/stocklog.csv'):
#     print(line, end=' ')

# for line in filematch('Work/Data/portfolio.csv','IBM'):
#     print(line, end=' ')

# lines = follow.follow('Work/Data/stocklog.csv')
# ibm = filematch(lines,'IBM')
# for line in ibm:
#     print(line)

