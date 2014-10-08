import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'app.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'CRYPTED'

DATABASE_PATH = os.path.join(basedir, DATABASE)

