""" create a SQLite3 database and table """

import sqlite3

# create a new database if doesn't already exist
conn = sqlite3.connect("new.db")

# use ":memory:" for in memory only
# disappear when the connection is closed
# conn = sqlite3.connect(":memory:")


# get a cursor object used to execute SQL commands
cursor = conn.cursor()


# create table
cursor.execute("""CREATE TABLE population
					(city TEXT, state TEXT, population INT)""")
conn.close()
