import os

#Get raw data 
os.system("curl --ftp-ssl anonymous:jupi@jupi.com "
          "ftp://ftp.nasdaqtrader.com/SymbolDirectory/nasdaqlisted.txt "
          "> data/nasdaq.lst")

os.system("curl --ftp-ssl anonymous:jupi@jupi.com "
          "ftp://ftp.nasdaqtrader.com/SymbolDirectory/otherlisted.txt "
          "> data/other.lst")



#removing the header and footers
os.system("tail -n +9 data/nasdaq.lst | cat | sed '$d' | sed 's/ /_/g' | sed 's/|/ /g' > "
          "data/nasdaq.lst2")

os.system("tail -n +9 data/other.lst | cat | sed '$d' | sed 's/ /_/g' | sed 's/|/ /g' > "
          "data/other.lst2")


#push it to a CSV
os.system("awk '{print $1}' data/nasdaq.lst2 > data/nasdaq.csv")

os.system("awk '{print $8}' data/other.lst2 > data/other.csv")

#remove .lst files
#os.system("rm data/*.lst data/*.lst2")