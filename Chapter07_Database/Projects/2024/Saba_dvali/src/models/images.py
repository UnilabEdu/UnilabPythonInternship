from src.ext import db
from src.models.base import BaseModel


class Images(db.Model):

    __tablename__ = "images"

    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.BLOB)

    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
