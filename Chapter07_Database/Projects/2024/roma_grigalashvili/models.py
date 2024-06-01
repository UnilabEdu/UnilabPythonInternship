from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from os import path

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + path.join(app.root_path, "db.sqlite")

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(200), nullable=False)
    choice1 = db.Column(db.String(100), nullable=False)
    choice2 = db.Column(db.String(100), nullable=False)
    choice3 = db.Column(db.String(100), nullable=False)
    choice4 = db.Column(db.String(100), nullable=False)
    correct_answer = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Question {self.id}: {self.question_text}>'

if __name__ == '__main__':
    db.create_all()
