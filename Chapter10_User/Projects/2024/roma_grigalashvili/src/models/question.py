from src.extensions import db
from src.models.base import BaseModel


class Question(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(200), nullable=False)
    choice1 = db.Column(db.String(100), nullable=False)
    choice2 = db.Column(db.String(100), nullable=False)
    choice3 = db.Column(db.String(100), nullable=False)
    choice4 = db.Column(db.String(100), nullable=False)
    correct_answer = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Question {self.id}: {self.question_text}>'