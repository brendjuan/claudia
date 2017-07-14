import os
import sys
import pandas_datareader.data as web
import datetime
from datetime import date
from datetime import timedelta
import pandas as pd
import time

start     = datetime.datetime(2010, 1, 1)
yesterday = date.today() - timedelta(days = 1)
end       = datetime.datetime(yesterday.year, yesterday.month, yesterday.day) 

ticks         = pd.read_csv("data/nasdaq.csv", index_col=None, header=None)
ticks.columns = ["Ticker"]

print()
print('UPDATING Nasdaq Stocks')

for index, row in ticks.iterrows():
	cant = 10
	comp = row['Ticker']
	
	if os.path.isfile('data/nasdaq/'+comp+'.csv'):
		temp  = pd.read_csv('data/nasdaq/'+ comp + '.csv')
		date  = temp.iloc[temp.shape[0] - 1][0]
		fin   = datetime.datetime.strptime(date, '%Y-%m-%d')
		delta = fin.date() - yesterday

		if delta != timedelta():
			s = yesterday + timedelta(days=1)

			while cant != 0:

				try:
					app = web.DataReader(comp, 'yahoo', s, fin)
					temp.append(app,ignore_index=True)
					print(temp)
					temp.to_csv('data/nasdaq/'+comp+'.csv')

				except:
					print ('Cant append')
					print (comp + ' ' + str(sys.exc_info()[0]))
					if cant == 1 :
						print ('FAILED: REACHED TIMEOUT ON ' + comp)

					cant = cant - 1	

	else:
		while (cant != 0):
			time.sleep(0.3)
			try:
				f = web.DataReader(comp, 'yahoo', start, end)
				f.to_csv('data/nasdaq/'+comp+'.csv')
				cant = 0
			except:
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
		temp  = pd.read_csv('data/other/'+comp+'.csv')
		date  = temp.iloc[temp.shape[0] - 1][0]
		fin   = datetime.datetime.strptime(date, '%Y-%m-%d')
		delta = fin.date() - yesterday

		if delta != timedelta():
			s = yesterday + timedelta(days=1)

			while cant != 0:
				try:
					app = web.DataReader(comp, 'yahoo', s, fin)
					temp.append(app,ignore_index=True)
					print(temp)
					temp.to_csv('data/other/'+comp+'.csv')
					
				except:
					print (comp + ' ' + str(sys.exc_info()[0]))
					if cant == 1 :
						print ('FAILED: REACHED TIMEOUT ON ' + comp)

					cant = cant - 1	

	else:
		while (cant != 0):
			time.sleep(0.3)
			try:
				f = web.DataReader(comp, 'yahoo', start, end)
				f.to_csv('data/other/'+comp+'.csv')
				cant = 0
			except:
				print (comp + ' ' + sys.exc_info()[0])
				if cant == 1 :
					print ('FAILED: REACHED TIMEOUT ON ' + comp)

				cant = cant - 1
	