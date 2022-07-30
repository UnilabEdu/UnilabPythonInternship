from source.models.base_model import BaseModel
from source import db


class User(BaseModel):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(24))
    email = db.Column(db.String(48))
    password = db.Column(db.String(48))
    experience = db.Column(db.String(24))
    account_type = db.Column(db.String(24))

