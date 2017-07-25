import os
import sys
import pandas_datareader.data as web
import datetime
from datetime import date
from datetime import timedelta
import pandas as pd
import time
import ntplib

x             = ntplib.NTPClient()
today         = datetime.datetime.utcfromtimestamp(x.request('north-america.pool.ntp.org').tx_time)
today         = today - timedelta(hours = 4) #offset to NYC time

start         = datetime.datetime(2010, 1, 1)
yesterday     = today.date() - timedelta(days = 1)

if (yesterday.weekday() == 5):
	yesterday = date.today() - timedelta(days = 2)

elif (yesterday.weekday() == 6):
	yesterday = date.today() - timedelta(days = 3)

end           = datetime.datetime(yesterday.year, yesterday.month, yesterday.day) 

ticks         = pd.read_csv("data/nasdaq.csv", index_col=None, header=None)
ticks.columns = ["Ticker"]

blacklist         = pd.read_csv("data/blacklist.csv", index_col=None, header=None)
blacklist.columns = ["Ticker"]

print()
print('UPDATING Nasdaq Stocks')

for index, row in ticks.iterrows():

	cant = 10
	comp = row['Ticker']
	
	if os.path.isfile('data/nasdaq/'+comp+'.csv'):

		temp  = pd.read_csv('data/nasdaq/'+ comp + '.csv', index_col=0)
		dates = list(temp.index)
		date  = dates[len(dates) - 1]
		fin   = datetime.datetime.strptime(date, '%Y-%m-%d')
		delta = fin.date() - yesterday

		if delta != timedelta():
			fin = fin.date() + timedelta(days=1)
			print(comp+ ' Updating')
			while cant != 0:
				try:
					app = web.DataReader(comp, 'yahoo', fin, yesterday)
					app.to_csv('temp.csv')
					app = pd.read_csv('temp.csv',index_col=0)
					temp = temp.append(app)
					temp.to_csv('data/nasdaq/'+comp+'.csv')

					cant = 0
				except:
					print (comp + ' ' + str(sys.exc_info()[0]))
					if cant == 1 :
						print ('FAILED: REACHED TIMEOUT ON ' + comp)
					cant = cant - 1	

	else:

		while (cant != 0):
			
			try:
				f = web.DataReader(comp, 'yahoo', start, end)
				f.to_csv('data/nasdaq/'+comp+'.csv')
				cant = 0
			except:
				time.sleep(0.01)
				print (comp + ' ' + str(sys.exc_info()[0]))
				if cant == 1 :
					print ('FAILED: REACHED TIMEOUT ON ' + comp)

				cant = cant - 1

print()
print('UPDATING Nasdaq Others')

ticks         = pd.read_csv("data/other.csv", index_col=None, header=None)
ticks.columns = ["Ticker"]
for index, row in ticks.iterrows():
	cant = 10
	comp = row['Ticker']
	
	if os.path.isfile('data/other/'+comp+'.csv'):
		temp  = pd.read_csv('data/other/'+ comp + '.csv', index_col=0)
		dates = list(temp.index)
		date  = dates[len(dates) - 1]
		fin   = datetime.datetime.strptime(date, '%Y-%m-%d')
		delta = fin.date() - yesterday

		if delta != timedelta():
			fin = fin.date() + timedelta(days=1)
			print(comp+ ' Updating')
			while cant != 0:
				try:
					app = web.DataReader(comp, 'yahoo', fin, yesterday)
					app.to_csv('temp.csv')
					app = pd.read_csv('temp.csv',index_col=0)
					temp = temp.append(app)
					temp.to_csv('data/other/'+comp+'.csv')

					cant = 0
				except:
					print (comp + ' ' + str(sys.exc_info()[0]))
					if cant == 1 :
						print ('FAILED: REACHED TIMEOUT ON ' + comp)
					cant = cant - 1		

	else:
		while (cant != 0):
			
			try:
				f = web.DataReader(comp, 'yahoo', start, end)
				f.to_csv('data/other/'+comp+'.csv')
				cant = 0
			except:
				time.sleep(0.01)
				print (comp + ' ' + str(sys.exc_info()[0]))
				if cant == 1 :
					print ('FAILED: REACHED TIMEOUT ON ' + comp)

				cant = cant - 1
	