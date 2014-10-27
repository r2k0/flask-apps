import sqlite3
from config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:

    c = connection.cursor()
    c.execute("""CREATE TABLE realtors(realtor_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, address TEXT NOT NULL, phone TEXT)""")

    c.execute('INSERT INTO realtors (name, address, phone)'
            'VALUES("YGN Realty", "800 Maha Rd, Yangon, Myanmar", "224311")')
