from cs50 import SQL 

db = SQL('sqlite:///instance/database.db')


db.execute('SELECT * FROM registrants')
