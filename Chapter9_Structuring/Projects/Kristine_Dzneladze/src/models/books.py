from src.extensions import db
from src.models.base import BaseModel

class Book(BaseModel):
    __tablename__  = "books"

    id = db.Column(db.Integer, primary_key=True)
    bookname = db.Column(db.String)
    author  = db.Column(db.String)
    genre = db.Column(db.String)
    img_link = db.Column(db.String)