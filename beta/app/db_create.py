import sqlite3
from config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:
    c = connection.cursor()

    c.execute("""CREATE TABLE properties(property_id INTEGER PRIMARY KEY AUTOINCREMENT,
            address TEXT NOT NULL, bed_rooms INTEGER , bath_rooms INTEGER,
            posted_date TEXT NOT NULL)""")
    c.execute(
            'INSERT INTO properties (address, bed_rooms, bath_rooms, posted_date)'
            'VALUES("123 Maha St, Yangon, Myanmar",3,3,"10/07/2014")'
            )
    c.execute(
            'INSERT INTO properties (address, bed_rooms, bath_rooms, posted_date)'
            'VALUES("456 Waha St, Mandalay, Myanmar",5,6,"10/07/2014")'
            )
