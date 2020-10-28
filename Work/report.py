# report.py
#
# Exercise 2.4
import fileparse
import csv
from pprint import pprint
# define a function to read file and represent the data with a list

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    '''
    return fileparse.parse_csv(filename,select=['name','shares','price'],types=[str,int,float])


def read_price(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    return dict(filename.parse_csv(filename,types=[str,float],has_headers = False))

def make_report_data(portfolio,prices): 
    '''
    MAKE A REPORT WITH PORTFOLIO AND PRICES
    '''
    rows =[]
    for stock in portfolio:
        current_price = (prices[stock['name']])
        change = current_price - (stock['price']) 
        summary = (stock['name'],stock['shares'],current_price,change)
        rows.append(summary)
    return report

def print_report(reportdata):
    '''
    Print a nicely formated table from a list of (name,shares,price,change) tuples.
    '''
    headers = ('Name','Shares','Price','Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-'*10+' ')*len(headers))
    for row in reportdata:
        print('%10s %10d %10.2f %10.2f'%row)

def portfolio_report(portfolio,pricefile):
    '''
    Make a stock report given portfolio and price data files
    '''
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_price(pricefile)

    # Creat the report data
    report = make_report_data(portfolio,prices)

    #print it out
    print_report(report)

def main(args):
    if len(args) != 3:
        raise SystemExit('Usage: %s portfolio pricefile' % args[0])
    portfolio_report(args[1],args[2])

if __name__ = '__main__':
    import sys
    main(sys.argv)



# file = '/home/jianye/practical-python/Work/Data/portfolio.csv'
# price_file = '/home/jianye/practical-python/Work/Data/prices.csv'
# stock_portfolio_in_list = read_portfolio_to_list(file)
# stock_portfolio_in_dict = read_portfolio_to_dict(file)
# stock_prices = read_price_to_dict(price_file)

# print(stock_portfolio_in_list)
# pprint(stock_portfolio_in_dict)
# pprint(stock_prices)
# total_cost=0.0

# # LOOP SOLUTION 1 --- calculate the total cost
# for s in stock_portfolio_in_list:
#     total_cost += s[1]*s[2]
# print(total_cost)
# # LOOP SOLUTION 2 --- calculate the total cost
# # total = 0.0
# # for name, shares, price in stock_portfolio:
# #     total_cost += shares*price
# # print(total_cost)

# gain = 0
# for s in stock_portfolio_in_list:
#     gain+=stock_prices[s[0]]*s[1]
# print(gain)

# diff = gain - total_cost

# if diff >0:
#     print("have gained ", diff )
# elif diff == 0:
#     print("No GAIN No LOSS")
# else:
#     print("have lost", diff)

# report = make_report(stock_portfolio_in_dict,stock_prices)
# # print normal table
# # for r in report:
# #     print(r)

# #print a  formatted table
# for r in report:
#     print('%10s %10d %10.2f %10.2f' % r)

# #with f format
# for name,shares,price,change in report:
#     print(f'{name:>10s}{shares:>10d}{price:>10.2f}{change:>10.2f}')

# header = ('Name','Share','Price','Change')
# print('%10s %10s %10s %10s' % header)
# print(('-' * 10 + ' ')*len(header))
# for r in report:
#     print('%10s %10d %10.2f %10.2f' % r)

# def make_a_new_report(filename):
#     f = open(filename)
#     rows = csv.reader(f)
#     headers=next(rows)
#     print(headers)
#     report=[]
#     for rowno, row in enumerate(rows,start = 1):
#         record = dict(zip(headers,row))
#         report.append(record)
#     return report

# filename = '/home/jianye/practical-python/Work/Data/portfoliodate.csv'
# print(make_a_new_report(filename))

# portfolio = read_portfolio_to_dict('/home/jianye/practical-python/Work/Data/portfolio.csv')

# from collections import Counter
# holdings = Counter()

# for s in portfolio:
#     holdings[s['name']] += s['shares']
# # print('Holdings-shares',holdings)
# # print('IBM',holdings['IBM'])
# # print('Most common',holdings.most_common(3))

# portfolio2 = read_portfolio_to_dict('/home/jianye/practical-python/Work/Data/portfolio2.csv')

# holding2 = Counter()

# for s in portfolio2:
#     holding2[s['name']]+=s['shares']
# # print(holding2)

# combind = holdings + holding2
# # print('Combined',combind)

# portfolio = read_portfolio_to_dict('/home/jianye/practical-python/Work/Data/portfolio.csv')
# cost = sum([s['shares']*s['price'] for s in portfolio])
# # print(cost)

# list = [s['shares']*s['price'] for s in portfolio]
# # print(list)

# more100 = [s for s in portfolio if s['shares']>100]
# # print(more100)

# msftibm = [s for s in portfolio if s['name'] in {'IBM','MSFT'}]
# # print(msftibm)


# cost10k = [s for s in portfolio if s['shares']*s['price']>10000]
# # print(cost10k)


# name_shares = [(s['name'],s['shares']) for s in portfolio]
# # print(name_shares)

# names = {s['name'] for s in portfolio}
# # print(names)

# holdings ={name:0 for name in names}
# # print(holdings)

# for s in portfolio:
#     holdings[s['name']] += s['shares']
# # print(holdings)

# import csv
# f = open('/home/jianye/practical-python/Work/Data/portfoliodate.csv')
# rows = csv.reader(f)
# # print(rows)
# headers = next(rows)
# # print(headers)


# select = ['name','shares','price']
# indices = [headers.index(colname) for colname in select]

# # print(indices)

# row = next(rows)
# record = {colname:row[index] for colname, index in zip(select, indices)}
# # print(record)


# portfolio = [{colname:row[index] for colname, index in zip(select,indices)}for row in rows]
# print(portfolio)


