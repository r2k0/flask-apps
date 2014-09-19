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

#insert data into table
c.executemany('INSERT INTO population VALUES(?,?,?)',cities)
