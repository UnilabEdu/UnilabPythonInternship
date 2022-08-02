from src.extensions import db
from src.models import BaseModel

class User(BaseModel):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    terms_agree = db.Column(db.Boolean, nullable=False)
    post = db.relationship('Post', backref='user', uselist=False)

    def __init__(self, name, password, email, terms_agree):
        self.name = name
        self.email = email
        self.password = password
        self.terms_agree = terms_agree

    def __repr__(self):
        return f'User Name: {self.name}'
