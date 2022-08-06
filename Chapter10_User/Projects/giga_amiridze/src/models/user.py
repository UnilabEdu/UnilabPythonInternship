from src.extensions import db, login_manager
from src.models import BaseModel
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(BaseModel, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password_hash = db.Column(db.String, nullable=False)
    terms_agree = db.Column(db.Boolean, nullable=False)
    post = db.relationship('Post', backref='user', uselist=False)

    def __init__(self, name, password, email, terms_agree):
        self.name = name
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.terms_agree = terms_agree

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @classmethod
    def find_by_email(cls, temp_email):
        email = cls.query.filter_by(email=temp_email).first()
        if email:
            return email

    def __repr__(self):
        return f'User Name: {self.name}'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
