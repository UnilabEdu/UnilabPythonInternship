from src.extensions import db
from src.models.base import BaseModel


class Teacher(BaseModel):

    __tablename__ = "teachers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)

    students = db.relationship("Student", backref="teacher")


class Student(BaseModel):

    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    course = db.Column(db.String)

    teacher_id = db.Column(db.Integer, db.ForeignKey("teachers.id"))
