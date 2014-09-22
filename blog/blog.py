# blog.py - controller

from flask import Flask, render_template, request, session, \
	flash, redirect, url_for, g
import sqlite3

#config
DATABASE = 'blog.db'

app = Flask(__name__)

# pulls in app configuration by looking for UPPERCASE variables
app.config.from_object(__name__)

def connect_db():
    """ db connection """
    return sqlite3.connect(app.config['DATABASE'])

@app.route('/')
def login():
    """ renders login page """
    return render_template('login.html')

@app.route('/main')
def main():
    # render_template(), Flask immediately recognizes
    # that login.html extends template.html, then fills 
    # int the block tags with the code found in login.html
    return render_template('main.html')

if __name__ == '__main__':
	app.run(debug=True)
