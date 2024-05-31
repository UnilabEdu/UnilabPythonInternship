from src.extensions import db
from src.models.base import BaseModel


class Product(BaseModel):

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String)
    description = db.Column(db.String)
    product_category = db.Column(db.String)
    page_category = db.Column(db.String)
    product_image = db.Column(db.String)


