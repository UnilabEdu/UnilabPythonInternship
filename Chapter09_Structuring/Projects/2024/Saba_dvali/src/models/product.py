from src.ext import db
from src.models.base import BaseModel


# class Products(db.Model):

#     __tablename__ = "products"

#     id = db.Column(db.Integer, primary_key=True)
#     product_name = db.Column(db.String)
#     product_model = db.Column(db.String)
#     price = db.Column(db.String)
#     info = db.Column(db.String)

#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))




class Products(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String)
    product_model = db.Column(db.String)
    price = db.Column(db.String)
    info = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    owner = db.relationship('Users', back_populates='products')
    images = db.relationship('Images', back_populates='product', lazy='dynamic')