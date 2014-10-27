import os

basedir = os.path.abspath(os.path.dirname(__file__))

#print basedir
DATABASE = 'test.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = TRUE
SECRET_KEY = 'booyah'

DATABASE_PATH = os.path.join(basedir, DATABASE)
