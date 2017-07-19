import os
import pandas_datareader.data as web
import datetime
from datetime import date
from datetime import timedelta
import pandas as pd
import time
import sys

t_delta       = 2*60

hr_offset     = 4
opening       = (9*60) + 30
closing       = (16*60) + 10

ticks         = pd.read_csv("data/nasdaq.csv", index_col=None, header=None)
ticks.columns = ["Ticker"]
tt            = list(ticks['Ticker'])
i             = 0

while i < len(tt):
	if not os.path.isfile('data/nasdaq/'+tt[i]+'.csv'):
		tt.pop(i)
	else:
		i += 1

i_delta = 80
x       = 0
y       = i_delta

last_t = time.time()

rt_quotes = web.get_quote_google('LITE') #LOL

while True:

	rightnow = datetime.datetime.now()
	conv_rnow = (rightnow.hour + hr_offset)*60 + rightnow.minute
	
	while (conv_rnow < opening):
		time.sleep(60*5)
		rightnow = datetime.datetime.now()
		conv_rnow = (rightnow.hour + hr_offset)*60 + rightnow.minute



	rt_quotes = web.get_quote_google('LITE') #LOL

	while (conv_rnow < closing):
		xx = web.get_quote_google(tt[x:y])
		rt_quotes = rt_quotes.append(xx)

		x  = y
		y += i_delta

		if y > len(tt): 
			y = len(tt)

		if x == len(tt):
			x = 0
			y = x + i_delta

			time.sleep(t_delta - (time.time() - last_t))

			last_t   = time.time()
			rightnow = datetime.datetime.now()

		rightnow = datetime.datetime.now()
		conv_rnow = (rightnow.hour + hr_offset)*60 + rightnow.minute


	rt_quotes.to_csv('data/daily/'+str(datetime.datetime.now().date())+'.csv')
	time.sleep(60*60*10)

print(xx.shape)
print(len(tt))
'''while True:
		

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
		#print('G: ' + str(lite2))'''