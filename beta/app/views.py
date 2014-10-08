from flask import Flask, flash, redirect, render_template,\
        request, session, url_for
from functools import wraps
import sqlite3

app = Flask(__name__)
app.config.from_object('config')

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


@app.route('/')
def beta():
    return render_template('index.html')

@app.route('/properties/')
def properties():
    pass
