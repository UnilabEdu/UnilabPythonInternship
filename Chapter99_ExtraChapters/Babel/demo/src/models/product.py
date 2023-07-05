from src.extensions import db
from src.models.base import BaseModel


class Product(db.Model, BaseModel):

    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    category = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Integer)

    def __repr__(self):
        return f"{self.name} (Price: {self.price})"