from flask_login import UserMixin
from uuid import uuid4

from werkzeug.security import generate_password_hash, check_password_hash
from app.models.base import BaseModel
from app.ext import db


class User(db.Model, BaseModel, UserMixin):

    __tablename__ = 'USERS'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    avatar = db.Column(db.String, default="avatar.png")
    developer_key = db.Column(db.String, default=str(uuid4()))

    favourite_movies = db.relationship('Movie', secondary='FAVOURITES')

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Favourite(db.Model):

    __tablename__ = 'FAVOURITES'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('USERS.id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('MOVIES.id'))
