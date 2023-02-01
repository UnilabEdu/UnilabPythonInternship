from teamapp.extensions import db
from .base import BaseModel


class Question(BaseModel):
    id=db.Column(db.Integer, primary_key=True)
    question=db.Column(db.Text)
    answer=db.Column(db.Text)
    asked_by_id=db.Column(db.Integer, db.ForeignKey('user.id'))
    mentor_id=db.Column(db.Integer, db.ForeignKey('user.id'))