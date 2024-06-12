from flask_login import UserMixin
from sqlalchemy import DateTime
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from src.ext import db
from src.models.base import BaseModel


class Users(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    _password = db.Column(db.String)
    age = db.Column(db.Integer)
    phone = db.Column(db.String)
    role = db.Column(db.Integer, db.ForeignKey('role.id'))
    date_joined = db.Column(DateTime, default=datetime.utcnow)

    products = db.relationship('Products', back_populates='owner', lazy='dynamic')
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)
        
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
    