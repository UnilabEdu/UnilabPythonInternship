from app import db


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    students = db.relationship("Student", backref="subject", lazy=True)
    # teacher = db.relationship("Teacher", backref="subject", lazy=True, uselist=False)
    # teacher_id = db.Column(db.Integer, db.ForeignKey("teacher.id"))

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return f" {self.title} created"


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey("subject.id"))

    def __init__(self, first_name, last_name, subject_id):
        self.first_name = first_name
        self.last_name = last_name
        self.subject_id = subject_id


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey("subject.id"), nullable=False)

    def __init__(self, first_name, last_name, subject_id):
        self.first_name = first_name
        self.last_name = last_name
        self.subject_id = subject_id