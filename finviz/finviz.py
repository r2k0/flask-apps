import urllib
import mechanize
import csv
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, \
        url_for, abort, render_template, flash, _app_ctx_stack

#app * Flask(__name__)
#app.config.from_object(__name__)

#url = "http://finviz.com/export.ashx?v=111&f=sh_price_u1"
url = "http://www.finviz.com/export.ashx?v=111&f=geo_usa,ind_exchangetradedfund,sh_curvol_o5000&o=-volume"
stockdata = urllib.urlopen(url).readlines()
print stockdata
