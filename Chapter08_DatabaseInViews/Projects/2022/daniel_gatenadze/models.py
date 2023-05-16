from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os



app = Flask(__name__)

projectdir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(projectdir, 'db.sqlite')
app.config['SECRET_KEY'] = "Secret_Password"

db = SQLAlchemy(app)



class SubsPlan(db.Model):
    __tablename__ = 'subsplan'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    price = db.Column(db.REAL)
    users = db.relationship('User', backref='sub_id')

    def __init__(self, name, price):
        self.name = name
        self.price = price


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(), unique=True)
    password = db.Column(db.String(64))
    gender = db.Column(db.String)
    age = db.Column(db.Integer)
    subscription_id = db.Column(db.Integer, db.ForeignKey('subsplan.id'))

    # def __init__(self, username, email, password, gender, age):
    #     self.username = username
    #     self.email = email
    #     self.password = password
    #     self.gender = gender
    #     self.age = age

    def create(self, commit=None, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        if commit is not None:
            self.save()

    @classmethod
    def read(cls, name):
        return cls.query.filter_by(name=name).first()  # could use .all()#

        # cls.query.filter(cls.age >= 2)

    def update(self, commit=None, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        if commit is not None:
            self.save()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()