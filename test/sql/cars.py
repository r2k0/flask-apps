""" 
Create a SQLite3 database "cars" and table "inventory"
include: "Make", "Model", and "Quantity" fields.
"""

import sqlite3

conn = sqlite3.connect("cars.db")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE inventory
	(make TEXT, model TEXT, quantity INT)""")

conn.close()
