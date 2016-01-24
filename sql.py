# Create SQLite table and populate it

import sqlite3

with sqlite3.connect("blog.db") as connection:
	c = connection.cursor()

	c.execute("""CREATE TABLE posts (title TEXT, post TEXT)""")

	c.execute('INSERT INTO posts VALUES ("Well","I am well, thanks.")')
	c.execute('INSERT INTO posts VALUES ("Good","I am good, thanks.")')
	c.execute('INSERT INTO posts VALUES ("Okay","I am okay, thanks.")')
	c.execute('INSERT INTO posts VALUES ("Excellent","I am excellent!")')