import os
import pandas_datareader.data as web
import datetime
from datetime import date
from datetime import timedelta
import pandas as pd
import time
while True:
	time.sleep(1)
	lite = web.get_quote_yahoo('LITE')
	#print('Y: ' + str(lite))

	lite2 = web.get_quote_google('LITE')
	print('G: ' + str(lite2))