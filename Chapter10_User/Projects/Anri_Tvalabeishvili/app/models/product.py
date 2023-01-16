from app.extensions import db
from app.models.base import BaseModel


class Game(BaseModel):
    __tablename__ = "Games"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    platform = db.Column(db.String)
    condition =  db.Column(db.String)
    exclusive = db.Column(db.String)
    price = db.Column(db.Integer)
    cuantity = db.Column(db.String)
    img =   db.Column(db.String)



class Gift(BaseModel):
    __tablename__ = "Gift Cards"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    type = db.Column(db.String)
    price = db.Column(db.Integer)
    region = db.Column(db.String)
    img =   db.Column(db.String)