# report.py
#
# Exercise 2.4
import csv
from pprint import pprint
# define a function to read file and represent the data with a list
def read_portfolio_to_list(filename):
    
    portfolio=[]
    with open(filename,'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = (row[0],int(row[1]),float(row[2]))
            portfolio.append(holding)
    return portfolio
# define a function
def read_portfolio_to_dict(filename):
    
    portfolio=[]
    with open(filename,'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {'name':row[0],'shares':int(row[1]),'price':float(row[2])}
            portfolio.append(holding)
    return portfolio

def read_price_to_dict(filename):

    prices = { }
    with open(filename,'rt') as f:
        rows= csv.reader(f)
        for row in rows:
            try:
                prices[row[0]]=float(row[1])
            except IndexError:
                pass         
    return prices

def make_report(portfolio,prices): 
    report =[]
    for stock in portfolio:
        current_price = float(prices[stock['name']])
        change = current_price - float(stock['price']) 
        summary = (stock['name'],stock['shares'],current_price,change)
        report.append(summary)
    return report


file = '/home/jianye/practical-python/Work/Data/portfolio.csv'
price_file = '/home/jianye/practical-python/Work/Data/prices.csv'
stock_portfolio_in_list = read_portfolio_to_list(file)
stock_portfolio_in_dict = read_portfolio_to_dict(file)
stock_prices = read_price_to_dict(price_file)

print(stock_portfolio_in_list)
pprint(stock_portfolio_in_dict)
pprint(stock_prices)
total_cost=0.0

# LOOP SOLUTION 1 --- calculate the total cost
for s in stock_portfolio_in_list:
    total_cost += s[1]*s[2]
print(total_cost)
# LOOP SOLUTION 2 --- calculate the total cost
# total = 0.0
# for name, shares, price in stock_portfolio:
#     total_cost += shares*price
# print(total_cost)

gain = 0
for s in stock_portfolio_in_list:
    gain+=stock_prices[s[0]]*s[1]
print(gain)

diff = gain - total_cost

if diff >0:
    print("have gained ", diff )
elif diff == 0:
    print("No GAIN No LOSS")
else:
    print("have lost", diff)

report = make_report(stock_portfolio_in_dict,stock_prices)
# print normal table
# for r in report:
#     print(r)

#print a  formatted table
for r in report:
    print('%10s %10d %10.2f %10.2f' % r)

#with f format
for name,shares,price,change in report:
    print(f'{name:>10s}{shares:>10d}{price:>10.2f}{change:>10.2f}')


header = ('Name','Share','Price','Change')
print('%10s %10s %10s %10s' % header)
print(('-' * 10 + ' ')*len(header))
for r in report:
    print('%10s %10d %10.2f %10.2f' % r)

def make_a_new_report(filename):
    f = open(filename)
    rows = csv.reader(f)
    headers=next(rows)
    print(headers)
    report=[]
    for rowno, row in enumerate(rows,start = 1):
        record = dict(zip(headers,row))
        report.append(record)
    return report

filename = '/home/jianye/practical-python/Work/Data/portfoliodate.csv'
print(make_a_new_report(filename))