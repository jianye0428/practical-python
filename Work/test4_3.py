import stock

s=stock.Stock('GOOG',100,490.1)
coloumns = ['name','shares']

for colname in coloumns:
    print(colname,'=',getattr(s,colname))