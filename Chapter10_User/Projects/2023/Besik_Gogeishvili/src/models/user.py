from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from src.extensions import db
from src.models.base import BaseModel


class User(BaseModel, UserMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    email = db.Column(db.String)
    sex = db.Column(db.String)
    _password = db.Column(db.String)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))

    role = db.relationship("Role", uselist = False)
    petitions = db.relationship("Petition", back_populates="user")


    @property
    def password(self):
        return self._password
    

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)


    def check_password_hash(self, password):
        return check_password_hash(self._password, password)
    

    def is_admin(self):
        return self.role_id == 1


    def __repr__(self) -> str:
        return self.username


class Role(BaseModel):

    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    user_role = db.Column(db.String)

    
    def __repr__(self) -> str:
        return self.user_role
