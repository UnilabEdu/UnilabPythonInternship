from sqalchemy import db


# Model File #


class SubsPlan(db.Model):
    __tablename__ = 'subsplan'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    price = db.Column(db.REAL)
    users = db.relationship('User', backref='subb')

    def __init__(self, name, price):
        self.name = name
        self.price = price


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(), unique=True)
    password = db.Column(db.String(64))
    gender = db.Column(db.String)
    age = db.Column(db.Integer)
    subscription_id = db.Column(db.Integer, db.ForeignKey('subsplan.id'))

    def __init__(self, username, subscription_id):
        self.username = username
        self.subscription_id = subscription_id
