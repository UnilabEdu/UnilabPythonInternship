from src.extentions import db
from src.models.base import BaseModel



class Product(BaseModel):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey("product_categories.id"))
    title = db.Column(db.String)
    color = db.Column(db.String)
    size = db.Column(db.String)
    price = db.Column(db.Integer)
    img = db.Column(db.String)
    category = db.relationship("ProductCategory", back_populates="products")


class ProductCategory(BaseModel):
    __tablename__ = "product_categories"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    products = db.relationship("Product", back_populates="category")

    def __repr__(self):
        return self.title
