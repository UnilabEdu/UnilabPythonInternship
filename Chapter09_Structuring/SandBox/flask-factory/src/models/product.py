from src.extensions import db
from src.models.base import BaseModel


class Product(BaseModel):

    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Integer)

    category_id = db.Column(db.Integer, db.ForeignKey('product_categories.id'))
    category = db.relationship("ProductCategory", uselist=False)

    def __repr__(self):
        return f"{self.name} - {self.category}"


class ProductCategory(BaseModel):

    __tablename__ = "product_categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
