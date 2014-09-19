# testing executemany() method

import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	# insert multiple records using a tuple
	cities = [
		('LA','CA',600000),
		('Boston','MA',2700000),
		('Houston','TX',210000),
		('Chicago','IL',250000),
		('Phoenix','AZ',150000)
	]

# insert data into table
c.executemany('INSERT INTO population VALUES(?,?,?)',cities)

# notes regarding placeholders: (?)
# (?), parameterized statements, act as placeholders
# for the tuple instead of string substitution (%s)
# string substitution exposes risk for potential 
# SQL injections that could occur from using string
# substitutions. For example: a user supplies a value
# looks like SQL code but really causes the SQL statement
# to behave in unexpected ways either accidental or malicious
# intent

