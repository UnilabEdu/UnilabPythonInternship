from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = "SecretKey"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+os.path.join(basedir, "data.sqlite")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


class Tutor(db.Model):
    __tablename__ = "tutors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    subject = db.Column(db.String)

    student = db.relationship('Student', backref='Tutor', uselist=False)

    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def __repr__(self):
        if self.student:
            return f"რეპეტიტორი {self.name} ასწავლის საგანს {self.subject} მოსწავლე {self.student.name}-ს ნომრით {self.student.id}"
        else:
            return f"რეპეტიტორს {self.name}-ს არ ჰყავს მოსწავლე"


class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    level = db.Column(db.String)

    tutor_id = db.Column(db.Integer, db.ForeignKey('tutors.id'))

    def __init__(self, name, level, tutor_id):
        self.name = name
        self.level = level
        self.tutor_id = tutor_id
