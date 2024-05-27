from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from src.extensions import db
from src.models.base import BaseModel


class User(BaseModel, UserMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    _password = db.Column(db.String)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password, password)