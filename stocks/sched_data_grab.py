import threading
import time

#Intraday stock ticker updating
#Frequency = every 2 or so minutes (defined later)
class update_intraday(threading.Thread):
	def __init__(self):

	def run(self):

#open, close, min, max stock ticker updating
#Frequency = everyday (defined later)
class update_daily(threading.Thread):
	def __init__(self):
		
	def run(self):

#Update all Nasdaq ticker listings 
#Frequency = weekly (defined later)
class update_tickers(threading.Thread):
	def __init__(self):
		
	def run(self):

#Main thread position
def main():
	



if __name__ == "__main__":
	main()