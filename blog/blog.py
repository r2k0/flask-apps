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

if __name__ == '__main__':
	app.run(debug=True)