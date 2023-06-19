from market.extensions import db
from flask_login import UserMixin
from market.models.base import BaseModel
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, BaseModel, UserMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    _password = db.Column(db.String, nullable=False)

    role_id = db.Column(db.ForeignKey('roles.id'))
    role = db.relationship("Role", uselist=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Role(db.Model, BaseModel):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
