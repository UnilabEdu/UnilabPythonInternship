from src.extensions import db
from src.models import BaseModel

class User(BaseModel):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)
    terms_agree = db.Column(db.Boolean, nullable=False)
    post = db.relationship('Post', backref='user', uselist=False)

    def __repr__(self):
        return f'User name: {self.name}'
