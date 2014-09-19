# Model

import sqlite3

# create blog.db with table 'posts'
# with two fields - 'title' and 'post'
with sqlite3.connect("blog.db") as connection:

	c = connection.cursor()
	c.execute("""CREATE TABLE posts
			(title TEXT, post TEXT)
			""")

	c.execute('INSERT INTO posts VALUES("WhatsUp","Waddup Dawg!")')
	c.execute('INSERT INTO posts VALUES("Oh no","OMG no")')
	c.execute('INSERT INTO posts VALUES("BooYEAH","THat\'s it")')
	c.execute('INSERT INTO posts VALUES("FOOBAR","Hello Foo, Hey Bar")')
