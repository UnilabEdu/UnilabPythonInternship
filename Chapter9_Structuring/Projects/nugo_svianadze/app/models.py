from flask_login import UserMixin
from app.extensions import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def create(self,commit=True, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
            
        if commit:
            db.session.add(self)
            db.session.commit()
        
    def delete(self,commit=True):
        db.session.delete(self)
        if commit:
            db.session.commit()
    
    def update(self,commit=True, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        if commit:
            db.session.commit()
    