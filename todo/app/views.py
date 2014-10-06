from flask import Flask, flash, redirect, render_template, request, \
        session, url_for
from functools import wraps
import sqlite3

app = Flask(__name__)
app.config.from_object('config')



