from src.extensions import db
from src.models.base import BaseModel


class Question(db.Model, BaseModel):
     
    __tablename__ = "question"

    id = db.Column(db.Integer, primary_key=True)  # Primary key for the Question model
    question_text = db.Column(db.String(200), nullable=False)  # Text of the question
    choice1 = db.Column(db.String(100), nullable=False)  # First choice
    choice2 = db.Column(db.String(100), nullable=False)  # Second choice
    choice3 = db.Column(db.String(100), nullable=False)  # Third choice
    choice4 = db.Column(db.String(100), nullable=False)  # Fourth choice
    correct_answer = db.Column(db.Integer, nullable=False)  # Correct answer index (1-4)

    quiz_id = db.Column(db.ForeignKey("quiz.id"), nullable=False)  # Foreign key to Quiz model
    quiz = db.relationship("Quiz", back_populates="questions")  # Relationship to Quiz model

    def __repr__(self):
        return f' {self.question_text}'
    
    #აბრუნებს ტექსტს სწორი პასუხის შესაბამისად ბაზიდან.
    def get_correct_answer(self):
        return getattr(self, f'choice{self.correct_answer}')
    