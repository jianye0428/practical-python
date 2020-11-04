# report.py
#
# Exercise 2.4
import fileparse
from stock import Stock
import csv
from pprint import pprint
import tableformat
# define a function to read file and represent the data with a list

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    '''
    with open(filename) as lines:
        portdicts = fileparse.parse_csv(lines, select=['name','shares','price'],types=[str,int,float])
    portfolio = [Stock(d['name'],d['shares'],d['price']) for d in portdicts]
    return portfolio

def read_price(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    with open(filename) as lines:
        return dict(filename.parse_csv(lines,types=[str,float],has_headers = False))

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
    return rows

def print_report(reportdata, formatter):
    '''
    Print a nicely formated table from a list of (name,shares,price,change) tuples.
    '''
    #headers = ('Name','Shares','Price','Change')
    #print('%10s %10s %10s %10s' % headers)
    #print(('-'*10+' ')*len(headers))
    formatter.headings(['Name','Shares','Price','Change'])
    for row, shares, price, change in reportdata:
        rowdata = [name, str(shares),f'{price:0.2f}',f'{price:0.2f}']
        formatter.row(rowdata)

def portfolio_report(portfoliofile,pricefile,fmt='txt'):
    '''
    Make a stock report given portfolio and price data files
    '''
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_price(pricefile)

    # Creat the report data
    report = make_report_data(portfolio,prices)

    #print it out
    #print_report(report)

    if fmt == 'txt':
        formatter = tableformat.TextTableFormatter()
    elif fmt == 'csv':
        formatter = tableformat.CSVTableFormatter()
    elif fmt == 'hrml':
        formatter = tableformat.HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown Format {fmt}')
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

def main(args):
    if len(args) != 3:
        raise SystemExit('Usage: %s portfolio pricefile' % args[0])
    portfolio_report(args[1],args[2])

if __name__ == '__main__':
    import sys
    main(sys.argv)



