from db import db

class Users(db.Model):
    id = db.Column(db.Integer,primary_key =True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
