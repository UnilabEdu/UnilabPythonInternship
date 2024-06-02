from flask_login import UserMixin
 
from src.ext import db
from src.models.base import BaseModel


# class Users(db.Model, UserMixin):

#     __tablename__ = "users"

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     email = db.Column(db.String)
#     password = db.Column(db.String)
#     role = db.Column(db.Integer, db.ForeignKey('role.id'))



class Users(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    role = db.Column(db.Integer, db.ForeignKey('role.id'))
    
    products = db.relationship('Products', back_populates='owner', lazy='dynamic')