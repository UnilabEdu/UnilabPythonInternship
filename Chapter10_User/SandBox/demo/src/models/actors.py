from src.extensions import db
from src.models.base import BaseModel


# MANY - TO - MANY Relationship
class Actor(db.Model, BaseModel):
    __tablename__ = "actors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    networth = db.Column(db.String)

    movies = db.relationship("Movie", secondary="movies_actors", back_populates="actors")

    def __repr__(self):
        return f"{self.name} {self.surname}"


class MovieActor(db.Model, BaseModel):

    __tablename__ = "movies_actors"

    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"))
    actor_id = db.Column(db.Integer, db.ForeignKey("actors.id"))


class Movie(db.Model, BaseModel):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    genre = db.Column(db.String)

    actors = db.relationship("Actor", secondary="movies_actors", back_populates="movies")

    def __repr__(self):
        return f"{self.name}"