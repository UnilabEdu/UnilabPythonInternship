from src.extensions import db
from src.models.base import BaseModel


class User(db.Model, BaseModel):
    __tabelname__ = "stats"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    weight_input = db.Column(db.String)
