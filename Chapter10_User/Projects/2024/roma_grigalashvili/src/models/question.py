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

    category_id = db.Column(db.ForeignKey("category.id"))
    category = db.relationship("Category", back_populates="question")

    def __repr__(self):
        return f'<Question {self.id}: {self.question_text}>'


class Category(db.Model, BaseModel):

    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String, unique=True)

    question = db.relationship("Question", back_populates="category")

    def __repr__(self):
        return f"{self.category}"


    