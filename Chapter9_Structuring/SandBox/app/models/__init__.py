from app.extensions import db


class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    teacher = db.relationship('Teacher', backref='student', lazy=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.teacher:
            return f"Student named {self.name} is a student of {self.teacher.name}"
        return f"Student named {self.name}"

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class Teacher(db.Model):
    __tablename__ = 'teachers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Teacher named {self.name}"
