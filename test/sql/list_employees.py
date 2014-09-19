import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	c.execute("SELECT firstname, lastname from employees")

	# fetchall() retrieves all records
	# storing as tuples within a tuple
	rows = c.fetchall()

	for r in rows:
		print r[0],r[1]
