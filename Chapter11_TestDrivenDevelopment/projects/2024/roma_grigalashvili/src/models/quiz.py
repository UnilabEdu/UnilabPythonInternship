from src.extensions import db
from src.models.base import BaseModel

class Quiz(db.Model, BaseModel):
     
    __tablename__ = "quiz"

    id = db.Column(db.Integer, primary_key=True)
    quiz_name = db.Column(db.String(50), nullable=False)

    category_id = db.Column(db.ForeignKey("category.id"), nullable=False)
    category = db.relationship("Category", back_populates="quiz")

    status = db.Column(db.Boolean, nullable=False, default=False)

    questions = db.relationship("Question", back_populates="quiz")

    def __repr__(self):
        return f'{self.quiz_name}'

class Category(db.Model, BaseModel):

    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String, unique=True)

    quiz = db.relationship("Quiz", back_populates="category")

    def __repr__(self):
        return f"{self.category}"

