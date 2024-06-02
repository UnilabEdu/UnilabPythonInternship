from src.ext import db
from src.models import BaseMod

class Products(db.Model,BaseMod):
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    price = db.Column(db.Integer)
    img = db.Column(db.String)



