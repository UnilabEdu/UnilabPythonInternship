from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from src.extensions import db
from src.models.base import BaseModel

# ONE - TO - ONE relationship
class User(db.Model, BaseModel, UserMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    _password = db.Column(db.String, nullable=False)

    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"), default=3)
    role = db.relationship("Role", uselist=False)
    scores = db.relationship('Score', back_populates='user')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"{self.username} {self.email}"


class Role(db.Model, BaseModel):

    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

    def __repr__(self):
        return f"{self.name}"