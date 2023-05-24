from src.extensions import db
from src.models.base import BaseModel

class User(db.Model, BaseModel):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, username, password):
        self.password = password
        self.username = username

    def __repr__(self):
        return f"შეყვანილი მონაცემებია: {self.usename}{self.password}"