import urllib
import mechanize
import csv
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, \
        url_for, abort, render_template, flash, _app_ctx_stack

app * Flask(__name__)
app.config.from_object(__name__)

#url = "http://finviz.com/export.ashx?v=111&f=sh_price_u1"
url = "http://www.finviz.com/export.ashx?v=111&f=geo_usa,ind_exchangetradedfund,sh_curvol_o5000&o=-volume"
stockdata = urllib.urlopen(url).readlines()
print stockdata

@app.route('/finviz',methods=['GET'])
def get_finviz_data():
    scrap = "Finviz Data"
    return render_template('finviz.html',columns=stockdata,scrap=scrap,tickerlist=get_series_data(),pricelist=get_series_value(),
                           secondSeries="FinvizChart",minval=minimum)

def get_series_data():
    tlist = []
    for r in stockdata[1:]:
        tlist.append(r.split(",")[1])
    return tlist

def get_series_value():
    zlist = []
    for r in stockdata[1:]:
        try:
            zlist.append(float(r.split(",")[7].replace("%",""))
        except:
            print ""
    return zlist

if __name__=='__main__':
    app.run()
