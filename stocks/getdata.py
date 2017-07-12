import os
import pandas_datareader.data as web
import datetime
from datetime import date
from datetime import timedelta

start = datetime.datetime(2010, 1, 1)
tempY = date.today() - timedelta(days = 1)
end   = datetime.datetime(tempY.year, tempY.month, tempY.day) 
print(start)
print(end)

f = web.DataReader('LITE', 'yahoo', start, end)
print (f)