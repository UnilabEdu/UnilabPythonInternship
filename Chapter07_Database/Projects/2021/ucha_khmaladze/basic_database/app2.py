import os
from flask_migrate import Migrate
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)
class UserModel(db.Model):

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username =db.Column(db.String)
    email = db.Column(db.String)
    age = db.Column(db.Integer)

    def __init__(self, username, email, age):

        self.username = username
        self.email = email
        self.age = age

    def __repr__(self):
        return f'User {self.username} with email: {self.email}'
