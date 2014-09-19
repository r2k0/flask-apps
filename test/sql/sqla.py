""" create a SQLite3 database and table """

import sqlite3

# create a new database if doesn't already exist
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# create table
cursor.execute("""CREATE TABLE population
					(city TEXT, state TEXT, pupulation INT)""")
conn.close()
