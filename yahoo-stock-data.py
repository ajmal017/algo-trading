'''
Yahoo stock data
Information at:
http://www.myhow2.net/wp/2013/07/python-how-to-look-up-stock-price-using-yahoo-stock-data-service/

input: a stock symbol
output: a dict of stock infomation
'''
import urllib2
from pymongo import MongoClient
import datetime
import csv
import pandas as pd

client = MongoClient('localhost',27017)

def getYahooStockQuote(symbol):
    url = "http://download.finance.yahoo.com/d/quotes.csv?s=" + symbol + "&f=sl1d1c1hgvr6r7j1"
    print url
    f = urllib2.urlopen(url)
    s = f.read()
    print s
    f.close()
    s = s.strip()
    L = s.split(',')
    D = {}
    D['symbol'] = L[0].replace('"','')
    D['last'] = L[1]
    D['date'] = L[2].replace('"','')
    D['change'] = L[3]
    D['high'] = L[4]
    D['low'] = L[5]
    D['vol'] = L[6]
    D['epsCurr'] = L[7]
    D['epsNext'] = L[8]
    D['marketCap'] = L[9]
    print D
    return D

#getYahooStockQuote('su')
#getYahooStockQuote('aapl')
#getYahooStockQuote('intc')

try:
    db = client.test
    collection = db.ystocks
    print "Connected Successfuly"
except pymongo.errors.ConnectionFailure, e:
    print "Could not connect to MongoDB: %s"

#stocks = collection.find({"Exchange": "NYQ", "Category Name": "Business Services"})
stocks = collection.find({"Type": "NYQ"})
print "Stocks %r" % stocks.count()

l = []

for stock in stocks:
    d = getYahooStockQuote(stock['Ticker'])
    l.append(dict(d))
    #Strip our B or M
    if (d['marketCap'] == 'N/A'):
        continue
    mkt_cap_str = d['marketCap'].translate(None, 'MB')
    mkt_cap = float(mkt_cap_str)
    if (mkt_cap >= 1.0 and d['epsCurr'] != 'N/A'): #Checking ONLY companies with a market cap of over $1B
        eps_next = float(d['epsCurr'])
        print stock['Ticker']
        print eps_next
        print mkt_cap

#http://stackoverflow.com/questions/18837262/convert-python-dict-into-a-dataframe
# df = pd.DataFrame(d.items())

df = pd.DataFrame(l, columns=['symbol','last','date','change','high','low','vol','epsCurr','epsNext','marketCap'])
df.to_csv('stocks.csv',sep=',')
