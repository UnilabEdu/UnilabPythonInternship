from src.ext import db
from src.models.base import BaseModel


class Role(db.Model):

    __tablename__ = "role"

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String)

