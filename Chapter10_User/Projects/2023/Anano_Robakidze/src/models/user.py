from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from src.models.base import BaseModel
from src.extentions import db



class User(BaseModel, UserMixin):

    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    _password = db.Column(db.String)

    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))
    role = db.relationship("Role", uselist=False)


    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)


    def check_password(self, password):
        return check_password_hash(self.password, password)

    def is_admin(self):
        return self.role and self.role.name == "Admin"


class Role(BaseModel):
     __tablename__ = "roles"

     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String)

     def __repr__(self):
         return self.name