"""
the handlers that respond to requests from browsers or clients.
Each view function is mapped to one or more request URLs.
"""
from flask import render_template
from app import app

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
