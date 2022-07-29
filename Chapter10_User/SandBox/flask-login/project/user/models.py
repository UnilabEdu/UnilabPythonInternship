from project import db, login_manager
from flask_login import UserMixin,
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), nullable=False, unique=True, index=True)
    username = db.Column(db.String(64), nullable=False, unique=True, index=True)
    password_hash = db.Column(db.String(225))
    role = db.Column(db.String(64), nullable=False, unique=False, default="user")

    def __init__(self, email, username, password, role="user"):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.role = role

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @classmethod
    def find_by_email(cls, temp_email):
        email = cls.query.filter_by(email=temp_email).first()
        if email:
            return email

    def is_admin(self):
        return self.role == "admin"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

