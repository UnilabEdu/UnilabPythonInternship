import sqlite3

connection = sqlite3.connect("db.sqlite")
cursor = connection.cursor()

cursor.execute(''' CREATE TABLE users(email text, password text)''')
