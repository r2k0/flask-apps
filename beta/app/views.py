from flask import Flask, flash, redirect, render_template,\
        request, session, url_for, g
from functools import wraps
import sqlite3


app = Flask(__name__)
app.config.from_object('config')

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.route('/')
def beta():
    return render_template('index.html')

@app.route('/forsale/')
def properties():
    g.db = connect_db()
    cur = g.db.execute( 'select address, bed_rooms, \
            bath_rooms, posted_date from properties' )
    properties = [dict(address=row[0], bed_rooms=row[1], \
            bath_rooms=row[2], posted_date=row[3]) for row in cur.fetchall()]
    g.db.close()
    return render_template(
            'forsale.html',
            properties=properties
            )
