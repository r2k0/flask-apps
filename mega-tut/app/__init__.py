"""
creates the application object (of class Flask) and then
imports the views module
"""

from flask import Flask

app = Flask(__name__)
from app import views
