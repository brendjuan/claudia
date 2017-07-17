import os
import pandas_datareader.data as web
import datetime
from datetime import date
from datetime import timedelta
import pandas as pd
import time
import sys

ticks         = pd.read_csv("data/nasdaq.csv", index_col=None, header=None)
ticks.columns = ["Ticker"]

while True:
	for index, row in ticks.iterrows():

		cant = 10
		comp = row['Ticker']
		if os.path.isfile('data/nasdaq/'+comp+'.csv'):
			try:
				data = web.get_quote_google(comp)
			except:
				print('failed on ' + comp)
				print (str(sys.exc_info()[0]))
			print(type(data))
	quit()
		#lite2 = web.get_quote_google('LITE')
		#print('G: ' + str(lite2))