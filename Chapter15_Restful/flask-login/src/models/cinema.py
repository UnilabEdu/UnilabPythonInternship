from src.extensions import db
from src.models.base import BaseModel


class ActorFilm(BaseModel):

    __tablename__ = "actors_films"

    id = db.Column(db.Integer, primary_key=True)
    actor_id = db.Column(db.Integer, db.ForeignKey("actors.id"))
    film_id = db.Column(db.Integer, db.ForeignKey("films.id"))


class Actor(BaseModel):

    __tablename__ = "actors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)

    # როდესაც გაქვს ასოციაციური თეიბლი, secondary-ში წერ მის __tablename__-ს
    films = db.relationship("Film", secondary="actors_films", backref="actors")

    def __repr__(self):
        return self.name


class Film(BaseModel):
    __tablename__ = "films"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    genre = db.Column(db.String)

    def __repr__(self):
        return self.name