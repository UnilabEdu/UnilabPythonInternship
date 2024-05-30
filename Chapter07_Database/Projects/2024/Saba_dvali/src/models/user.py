from src.ext import db
from src.models.base import BaseModel


class Users(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)

    role = db.Column(db.Integer, db.ForeignKey('role.id'))
    # role = db.relationship('Role', backref=db.backref('users', lazy=True))


    