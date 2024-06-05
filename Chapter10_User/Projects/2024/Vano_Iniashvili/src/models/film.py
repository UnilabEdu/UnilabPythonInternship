from src.extensions import db
from src.models.base import BaseModel
from src.models.user import User


class Film(BaseModel):
    __tablename__ = "films"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    director = db.Column(db.String)
    genre = db.Column(db.String)
    release_date = db.Column(db.DateTime)
    cover = db.Column(db.String())


class UserFilm(BaseModel):
    __tablename__ = 'users_films'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    film_id = db.Column(db.Integer, db.ForeignKey('films.id'))