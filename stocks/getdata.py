import os
import pandas_datareader.data as web
import datetime
from datetime import date
from datetime import timedelta
import pandas as pd

start = datetime.datetime(2010, 1, 1)
tempY = date.today() - timedelta(days = 1)
end   = datetime.datetime(tempY.year, tempY.month, tempY.day) 
print(start)
print(end)

data = pd.read_csv("data/nasdaq.csv", index_col=None, header=None)
data.columns = ["Ticker"]
for index, row in data.iterrows():
	print(row['Ticker'])
	comp = row['Ticker']
	print(type(comp))
	f = web.DataReader(comp, 'yahoo', start, end)
	f.to_csv('data/nasdaq/'+comp+'_'+str(end)+'.csv')