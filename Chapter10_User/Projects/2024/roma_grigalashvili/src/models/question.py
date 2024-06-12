from src.extensions import db
from src.models.base import BaseModel


class Question(db.Model, BaseModel):
     
    __tablename__ = "question"

    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(200), nullable=False)
    choice1 = db.Column(db.String(100), nullable=False)
    choice2 = db.Column(db.String(100), nullable=False)
    choice3 = db.Column(db.String(100), nullable=False)
    choice4 = db.Column(db.String(100), nullable=False)
    correct_answer = db.Column(db.Integer, nullable=False)

    quiz_id = db.Column(db.ForeignKey("quiz.id"), nullable=False)
    quiz = db.relationship("Quiz", back_populates="questions")

    def __repr__(self):
        return f' {self.question_text}'



    