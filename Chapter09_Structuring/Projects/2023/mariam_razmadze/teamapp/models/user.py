from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from teamapp.extensions import db
from .base import BaseModel


class User(UserMixin, BaseModel):
    id=db.Column(db.Integer, primary_key=True, unique=True)
    name=db.Column(db.String(50))
    password=db.Column(db.String(280))
    senior=db.Column(db.Boolean)
    junior=db.Column(db.Boolean)
    intern=db.Column(db.Boolean)
    admin=db.Column(db.Boolean)

    questions_asked=db.relationship('Question', foreign_keys='Question.asked_by_id', backref='asker', lazy=True)
    answers_expected=db.relationship('Question', foreign_keys='Question.mentor_id', backref='mentor', lazy=True)

    @property
    def unhashed_password(self):
        raise AttributeError('Unhashed password!')
    
    @unhashed_password.setter
    def unhashed_password(self, unhashed_password):
        self.password=generate_password_hash(unhashed_password)
