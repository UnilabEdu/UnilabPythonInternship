from src.ext import db
from src.models.base import BaseModel


# class Images(db.Model):

#     __tablename__ = "images"

#     id = db.Column(db.Integer, primary_key=True)
#     image = db.Column(db.BLOB)

#     product_id = db.Column(db.Integer, db.ForeignKey('products.id'))




class Images(db.Model):
    __tablename__ = "images"
    id = db.Column(db.Integer, primary_key=True)
    image_name = db.Column(db.String)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    product = db.relationship('Products', back_populates='images')