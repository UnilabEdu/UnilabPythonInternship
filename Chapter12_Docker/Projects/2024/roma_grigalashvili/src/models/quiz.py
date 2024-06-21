from src.extensions import db
from src.models.base import BaseModel
from src.models.user import User

class Quiz(db.Model, BaseModel):
     
    __tablename__ = "quiz"

    id = db.Column(db.Integer, primary_key=True)
    quiz_name = db.Column(db.String(50), nullable=False)
    quiz_text = db.Column(db.String(200), nullable=False)  # Text of the quiz

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)  # Reference to User model
    user = db.relationship("User", back_populates="quiz")  # Relationship to User model

    category_id = db.Column(db.ForeignKey("category.id"), nullable=False)
    category = db.relationship("Category", back_populates="quiz")

    status = db.Column(db.Boolean, nullable=False, default=False)

    questions = db.relationship("Question", back_populates="quiz")
    scores = db.relationship("Score", back_populates="quiz")

    def __repr__(self):
        return f'{self.quiz_name}'

class Category(db.Model, BaseModel):

    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String, unique=True)

    quiz = db.relationship("Quiz", back_populates="category")

    def __repr__(self):
        return f"{self.category}"

class Score(db.Model, BaseModel):
    __tablename__ = "scores"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    time_taken = db.Column(db.Float, nullable=True)

    user = db.relationship('User', back_populates='scores')
    quiz = db.relationship('Quiz', back_populates='scores')