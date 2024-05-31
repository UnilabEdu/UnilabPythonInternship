from src.ext import db
from src.models.base import BaseModel


class Product(db.Model, BaseModel):

    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    category = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Integer)
    img = db.Column(db.String)

    user = db.relationship("User", secondary="user_products", back_populates="products", uselist=False)
    product_images = db.relationship("ProductImage", back_populates="product")

    def __repr__(self):
        return f"{self.name} (Price: {self.price})"


class ProductImage(db.Model, BaseModel):

    __tablename__ = "product_images"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    product_id = db.Column(db.ForeignKey("products.id"))
    product = db.relationship("Product", back_populates="product_images")

class UserProduct(db.Model, BaseModel):

    __tablename__ = "user_products"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey("users.id"))
    product_id = db.Column(db.ForeignKey("products.id"))