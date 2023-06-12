from flask_login import UserMixin
from src.extensions import db
from src.models.base import BaseModel
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, BaseModel, UserMixin):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    _password = db.Column(db.String)
    gender = db.Column(db.String)
    birthday = db.Column(db.Date)

    role_id = db.Column(db.ForeignKey("roles.id"))
    role = db.relationship("Role", uselist=False)

    idcard_id = db.Column(db.ForeignKey("id_cards.id"))
    idcard = db.relationship("IDCard", back_populates="user")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)


def check_password(self, password):
    return check_password_hash(self.password, password)


def __init__(self, username, password):
    self.password = password
    self.username = username


def __repr__(self):
    return f"შეყვანილი მონაცემებია: {self.username}{self.password}"


class Role(db.Model, BaseModel):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)


    def __repr__(self):
        return f"{self.name}"

class IDCard(db.Model):
    __tablename__ = "id_cards"

    id = db.Column(db.Integer, primary_key=True)
    id_number = db.Column(db.String, unique=True)
    creation_date = db.Column(db.Date)
    expiry_date = db.Column(db.Date)

    user = db.relationship("User", back_populates="idcard")

    def __repr__(self):
        return f"პირადობა, ნომრით {self.id_number}"
