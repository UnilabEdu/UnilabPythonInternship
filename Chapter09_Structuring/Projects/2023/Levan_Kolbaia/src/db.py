import sqlite3
from App import db, app,user_input,nutrition

with app.app_context():
    db.create_all()

conn=sqlite3.connect("database.db")
ccursor=conn.cursor()

