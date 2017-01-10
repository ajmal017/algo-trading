'''
Plotting a stock
'''
import matplotlib.pyplot as plt
import numpy as np
import urllib2
import datetime

# http://www.myhow2.net/wp/2013/07/python-how-to-look-up-stock-price-using-yahoo-stock-data-service/
flags = "&f=sl1d1c1hgvr6r7j1b2b3a2ghm2m3abc6f6i5ops7w4"

def getYahooStockQuote(symbol):
    url = "http://download.finance.yahoo.com/d/quotes.csv?s=" + symbol + flags
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
    D['realTimeAsk'] = L[10]
    D['realTimeBid'] = L[11]
    D['averageDailyVolume'] = L[12]
    D['dailyLow'] = L[13]
    D['dailyHigh'] = L[14]
    D['reatimeDailyRange'] = L[15]
    D['movingAverage50Days'] = L[16]
    D['ask'] = L[17]
    D['bid'] = L[18]
    D['realtimeChange'] = L[19]
    D['floatShares'] = L[20]
    D['realtimeOrderBook'] = L[21]
    D['open'] = L[22]
    D['previousClose'] = L[23]
    D['realtimeOrderBook'] = L[24]
    D['shortRatio'] = L[25]
#    D['daysValueChange'] = L[26]

    print D
    return D

l = []

#d = getYahooStockQuote(stock['Ticker'])

plt.ion() ## Note this correction
fig=plt.figure()
#  range    X       Y
plt.axis([0,100,35,130])

i=0
x=list()
y=list()
x1=list()
y1=list()

while (i < 100):
    d = getYahooStockQuote('INTC')
    #Draw the stock last value
    temp_y=d['last']
    x.append(i);
    y.append(temp_y);
    plt.scatter(i,temp_y);
    #Draw the volume
    temp_y1=int(d['vol'])/100000
    x1.append(i);
    y1.append(temp_y1);
    plt.scatter(i,temp_y1);
    i+=1;
    plt.show()
    plt.pause(0.0001) #Note this correction

raw_input() #keep the window open
