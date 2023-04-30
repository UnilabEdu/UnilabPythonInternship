from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Tutor(db.Model, UserMixin):
    __tablename__ = "tutors"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False, unique=True, index=True)
    email = db.Column(db.String(64), nullable=False, unique=True, index=True)
    password_hash = db.Column(db.String(255))
    subject = db.Column(db.String)

    student = db.relationship('Student', backref='Tutor', uselist=False)

    def __init__(self, username, email, password, subject):
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.subject = subject

    def add_tutor(self):
        db.session.add(self)
        db.session.commit()

    def delete_tutor(self):
        db.session.delete(self)
        db.session.commit()

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @classmethod
    def find_by_email(cls, temp_email):
        email = cls.query.filter_by(email=temp_email).first()
        if email:
            return email


@login_manager.user_loader
def load_user(user_id):
    return Tutor.query.get(user_id)


class Student(db.Model, UserMixin):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False, unique=True, index=True)
    email = db.Column(db.String(64), nullable=False, unique=True, index=True)
    password_hash = db.Column(db.String(255))
    tutor_id = db.Column(db.Integer, db.ForeignKey('tutors.id'))

    def __init__(self, username, email, password, tutor_id):
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.tutor_id = tutor_id

    def add_student(self):
        db.session.add(self)
        db.session.commit()

    def delete_student(self):
        db.session.delete(self)
        db.session.commit()

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @classmethod
    def find_by_email(cls, temp_email):
        email = cls.query.filter_by(email=temp_email).first()
        if email:
            return email


@login_manager.user_loader
def load_user(user_id):
    return Student.query.get(user_id)
