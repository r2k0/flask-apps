# application's config

import os
# grabs the folder where the script runs
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'todo.db'
USERNAME = 'admin'
PASSWORD = 'admin'

# WTF_CSRF_ENABLED config setting is used for 
# cross-site request forgery prevention
# the SECRET_KEY config setting is used in conjunction
# with the WTF_CSRF_ENABLED setting in order to create
# a cryptographic token that is used to validate a form.
WTF_CSRF_ENABLED = True
SECRET_KEY = 'SECRET_KEY'

DATABASE_PATH = os.path.join(basedir, DATABASE)
