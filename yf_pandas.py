import pandas_datareader as pdr
from  pandas_datareader import data
from datetime import datetime

# ibm = pdr.get_data_yahoo(symbols='IBM', start=datetime(2000, 1, 1), end=datetime(2012, 1, 1))
# print(ibm['Adj Close'])

#In [13]: aapl = data.DataReader('AAPL', 'yahoo', '1980-01-01')

# yahoo api is inconsistent for getting historical data, please use google instead.
aapl = data.DataReader('AAPL', 'google', '1980-01-01')
print(aapl)