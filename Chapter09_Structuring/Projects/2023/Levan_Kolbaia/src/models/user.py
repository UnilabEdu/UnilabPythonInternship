from src.extension import db
from src.models.base import BaseModel

class user_input(db.Model,BaseModel):
    __tabelname__ = "stats"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    weight_input= db.Column(db.String)

