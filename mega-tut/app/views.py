"""
the handlers that respond to requests from browsers or clients.
Each view function is mapped to one or more request URLs.
"""

from app import app

#the two decorators create mappings from URLs / and /index to this function
@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
