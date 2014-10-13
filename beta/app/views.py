from flask import Flask, flash, redirect, render_template,\
        request, session, url_for, g, jsonify
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
    g.db = connect_db()
    cur = g.db.execute( 'select address, bed_rooms, \
            bath_rooms, posted_date from properties' )
    properties = [dict(address=row[0], bed_rooms=row[1], \
            bath_rooms=row[2], posted_date=row[3]) for row in cur.fetchall()]
    g.db.close()
    return render_template(
            'properties.html',
            properties=properties
            )

@app.route('/rentals/')
def rentals():
    g.db = connect_db()
    cur = g.db.execute( 'select address, bed_rooms, \
            bath_rooms, posted_date from properties' )
    properties = [dict(address=row[0], bed_rooms=row[1], \
            bath_rooms=row[2], posted_date=row[3]) for row in cur.fetchall()]
    g.db.close()
    return render_template(
            'rentals.html',
            properties=properties
            )

def login_required(test):
    @wrap(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
        return wrap

@app.route('/logout/')
def logout():
    session.pop('logged_in', None)
    flash('Logged Out: ')
    return redirect(url_for('login'))

@app.route('/login/',methods=['GET','POST']
def login():
    if requested.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] \
                or request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid Credentials.'
            return render_template('login.html',error=error)
    else:
        session['logged_in'] = True
        return redirect(url_for('tasks'))
    if request.method == 'GET':
        return render_template('login.html')





