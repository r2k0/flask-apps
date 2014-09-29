import urllib2
import csv
import pandas as pd

def get_etfs(file):
    url = "http://www.finviz.com/export.ashx?v=150&f=geo_usa,ind_exchangetradedfund,sh_curvol_o5000&o=-volume"
    rawdata = urllib2.urlopen(url).readlines()
    file = open(file,'wb')
    for l in rawdata:
        l= l.replace("\"","")
        print l
        file.write(l)
    file.close()

def main():
    get_etfs("etfdata.txt")

if __name__ == '__main__':
    main()
