from src.ext import db


class Users(db.Model):
      id = db.Column(db.Integer, primary_key = True)
      username = db.Column(db.String)
      password = db.Column(db.String)
      age = db.Column(db.Date)
      gender = db.Column(db.String)
      nationality = db.Column(db.String)

    




