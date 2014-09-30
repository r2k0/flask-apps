"""
the handlers that respond to requests from browsers or clients.
Each view function is mapped to one or more request URLs.
"""
from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

#the two decorators create mappings from URLs / and /index to this function
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Okkar'}

    posts = [
            {
                'author': {'nickname': 'Max'},
                'body': 'Golden Gate Bridge!'
            },
            {
                'author': {'nickname': 'Pan'},
                'body': 'I want bacon!'
            }
            ]
    return render_template('index.html',
                            title='Home',
                            user=user,
                            posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html',
                           title='Sign In',
                           form=form)
