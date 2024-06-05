from src.extensions import db
from flask_login import UserMixin
from src.models.base import BaseModel
from werkzeug.security import generate_password_hash, check_password_hash


class User(BaseModel, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    _password = db.Column(db.String)
    films = db.relationship("Film", secondary="users_films", backref="users")

    def _get_password(self):
        return self._password

    def _set_password(self, password):
        self._password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    password = db.synonym('_password', descriptor=property(_get_password, _set_password))