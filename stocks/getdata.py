import os
import sys
import pandas_datareader.data as web
import datetime
from datetime import date
from datetime import timedelta
import pandas as pd
import time
import ntplib

tolerance     = 3

x             = ntplib.NTPClient()
today         = datetime.datetime.utcfromtimestamp(x.request('north-america.pool.ntp.org').tx_time)
today         = today - timedelta(hours = 4) #offset to NYC time

start         = datetime.datetime(1980, 1, 1)
yesterday     = today.date() - timedelta(days = 1)

if (yesterday.weekday() == 5):
	yesterday = today.date() - timedelta(days = 2)

elif (yesterday.weekday() == 6):
	yesterday = today.date() - timedelta(days = 3)

end           = datetime.datetime(yesterday.year, yesterday.month, yesterday.day) 

ticks         = pd.read_csv("data/nasdaq.csv", index_col=None, header=None)
ticks.columns = ["Ticker"]

blackl         = pd.read_csv("data/blacklist.csv", index_col=0)
blackl.columns = ["Ticker"]
list_blackl    = list(blackl['Ticker'])

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
			if comp in list_blackl :
				cant = tolerance

			fin = fin.date() + timedelta(days=1)
			print(comp+ ' Updating')
			while cant != 0:
				try:
					app = web.DataReader(comp, 'yahoo', fin, yesterday)
					app.to_csv('temp.csv')
					app = pd.read_csv('temp.csv',index_col=0)
					temp = temp.append(app)
					temp.to_csv('data/nasdaq/'+comp+'.csv')
					if comp in list_blackl:
						list_blackl.remove(comp)
					cant = 0
				except:
					#print (comp + ' ' + str(sys.exc_info()[0]))
					if cant == 1 :
						print ('FAILED: REACHED TIMEOUT ON ' + comp)
						if not comp in list_blackl:
							list_blackl.append(comp)
							print('Appended ' + comp + ' to blacklist')
						else:
							print(comp + ' is already on blacklist')
					cant = cant - 1	

	else:
		if comp in list_blackl :
			cant = tolerance 

		while (cant != 0):
			
			try:
				f = web.DataReader(comp, 'yahoo', start, end)
				f.to_csv('data/nasdaq/'+comp+'.csv')
				if comp in list_blackl:
					list_blackl.remove(comp)
				cant = 0
			except:
				time.sleep(0.01)
				#print (comp + ' ' + str(sys.exc_info()[0]))
				if cant == 1 :
					print ('FAILED: REACHED TIMEOUT ON '+ comp)
					if not comp in list_blackl:
						list_blackl.append(comp)
						print('Appended ' + comp + ' to blacklist')
					else:
						print(comp + ' is already on blacklist')

				cant = cant - 1

print('Updating Blacklist')
out = pd.DataFrame.from_records([list_blackl]).T
out.to_csv('data/blacklist.csv')

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
			if comp in list_blackl :
				cant = tolerance

			fin = fin.date() + timedelta(days=1)
			print(comp+ ' Updating')
			while cant != 0:
				try:
					app = web.DataReader(comp, 'yahoo', fin, yesterday)
					app.to_csv('temp.csv')
					app = pd.read_csv('temp.csv',index_col=0)
					temp = temp.append(app)
					temp.to_csv('data/other/'+comp+'.csv')
					if comp in list_blackl:
						list_blackl.remove(comp)
					cant = 0
				except:
					#print (comp + ' ' + str(sys.exc_info()[0]))
					if cant == 1 :
						print ('FAILED: REACHED TIMEOUT ON ' + comp)
						if not comp in list_blackl:
							list_blackl.append(comp)
							print('Appended ' + comp + ' to blacklist')
						else:
							print(comp + ' is already on blacklist')
					
					cant = cant - 1		

	else:
		if comp in list_blackl :
			cant = tolerance

		while (cant != 0):
			
			try:
				f = web.DataReader(comp, 'yahoo', start, end)
				f.to_csv('data/other/'+comp+'.csv')
				if comp in list_blackl:
					list_blackl.remove(comp)
				cant = 0
			except:
				time.sleep(0.01)
				#print (comp + ' ' + str(sys.exc_info()[0]))
				if cant == 1 :
					print ('FAILED: REACHED TIMEOUT ON ' + comp)
					if not comp in list_blackl:
						list_blackl.append(comp)
						print('Appended ' + comp + ' to blacklist')
					else:
						print(comp + ' is already on blacklist')

				cant = cant - 1

print('Updating Blacklist')
out = pd.DataFrame.from_records([list_blackl]).T
out.to_csv('data/blacklist.csv')
	