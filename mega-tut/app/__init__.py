"""
creates the application object (of class Flask) and then
imports the views module
"""

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app import views
