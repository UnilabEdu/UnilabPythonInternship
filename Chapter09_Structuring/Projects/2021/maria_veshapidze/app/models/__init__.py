from app import db


class Tutor(db.Model):
    __tablename__ = "tutors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    subject = db.Column(db.String)

    student = db.relationship('Student', backref='Tutor', uselist=False)

    def __init__(self, name, email, password, subject):
        self.name = name
        self.email = email
        self.password = password
        self.subject = subject

    def add_tutor(self):
        db.session.add(self)
        db.session.commit()

    def delete_tutor(self):
        db.session.delete(self)
        db.session.commit()


class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)

    tutor_id = db.Column(db.Integer, db.ForeignKey('tutors.id'))

    def __init__(self, name, email, password, tutor_id):
        self.name = name
        self.email = email
        self.password = password
        self.tutor_id = tutor_id

    def add_student(self):
        db.session.add(self)
        db.session.commit()

    def delete_student(self):
        db.session.delete(self)
        db.session.commit()
