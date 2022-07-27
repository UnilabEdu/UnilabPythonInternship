from source.models.base_model import BaseModel
from source import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from source import login_manager


class User(BaseModel, UserMixin):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(24))
    email = db.Column(db.String(48))
    password = db.Column(db.String(48))
    experience = db.Column(db.String(24))
    account_type = db.Column(db.String(24))

    def __init__(self, username, email, password, experience, account_type):
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.experience = experience
        self.account_type = account_type

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @classmethod
    def find_by_email(cls, temp_email):
        email = cls.query.filter_by(email=temp_email).first()
        if email:
            return email


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

