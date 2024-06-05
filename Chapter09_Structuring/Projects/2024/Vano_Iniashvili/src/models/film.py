from src.extensions import db


class Film(db.Model):
    __tablename__ = "films"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    director = db.Column(db.String)
    genre = db.Column(db.String)
    release_date = db.Column(db.DateTime)
    cover = db.Column(db.String())