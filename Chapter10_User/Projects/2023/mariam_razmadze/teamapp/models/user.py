from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from teamapp.extensions import db
from .base import BaseModel


class User(BaseModel, UserMixin):

    __tablename__ = 'user'

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50), unique=True, nullable=False)
    email=db.Column(db.String, unique=True)
    _password=db.Column(db.String(280))


    questions_asked=db.relationship('Question', foreign_keys='Question.asked_by_id', backref='asker', lazy='dynamic')
    answers_expected=db.relationship('Question', foreign_keys='Question.mentor_id', backref='mentor', lazy='dynamic')
    roles=db.relationship("Role", secondary='user_roles', backref='users_with_role')


    def _get_password(self):
        return self._password
    

    def _set_password(self, password):
        self._password=generate_password_hash(password)
    

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def has_role(self, role):
        return role in [userrole.name for userrole in self.roles]
    
    

    password=db.synonym('_password', descriptor=property(_get_password, _set_password))

    def __repr__(self):
        return self.name
 



class UserRole(BaseModel):
    __tablename__="user_roles"
    id = db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))
    role_id=db.Column(db.Integer, db.ForeignKey('roles.id'))

class Role(BaseModel):

    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)


    def __repr__(self):
        return self.name
 

