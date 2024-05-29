from src.extensions import db
from src.models.base import BaseModel


class Works(BaseModel):

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String)
    description = db.Column(db.String)
    product_category= db.Column(db.String)
    product_image = db.Column(db.String)
    product_video = db.Column(db.String)
    release_year = db.Column(db.String)
    director = db.Column(db.String)
