from app.models.base import BaseModel
from app.ext import db


class Movie(db.Model, BaseModel):

    __tablename__ = 'MOVIES'

    id = db.Column(db.Integer, primary_key=True)
    picture = db.Column(db.String)
    name = db.Column(db.String)
    rating = db.Column(db.Float)
    genre = db.Column(db.String)
    release_date = db.Column(db.DateTime)

    def __init__(self, name, genre, rating, picture):
        self.name = name
        self.genre = genre
        self.rating = rating
        self.picture = picture
