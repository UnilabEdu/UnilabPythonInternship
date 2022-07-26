from app.extentions import db, login_manager
from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    __tablename__ = "users_1"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), nullable=False, unique=True, index=True)
    username = db.Column(db.String(64), nullable=False, unique=True, index=True)
    password_hash = db.Column(db.String(225))

    role = db.Column(db.String(64), nullable=False, default="user")

    def __init__(self, email, username, password, role="user"):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.role = role

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @classmethod
    def find_by_email(cls, temp_email):
        email = cls.query.filter_by(email=temp_email).first()
        if email:
            return email


    def is_admin(self):
        return self.role == 'admin'

    def save(self):
        db.session.add(self)
        db.session.commit()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)





class BaseModel():

    id = db.Column(db.Integer, primary_key=True)
    def create(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

            self.save()
    @classmethod
    def read_all(cls):
        return cls.query.all()

    @classmethod
    def read(cls, name):
        return cls.query.filter_by(name=name).first()

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

            self.save()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def save(self):
        db.session.add(self)
        db.session.commit()


class Coach(db.Model, BaseModel):
    __tablename__ = 'coaches'
    name = db.Column(db.String(24))
    age = db.Column(db.Integer)




class Pupil(db.Model, BaseModel):
    __tablename__ = 'pupils'

    name = db.Column(db.String(32))
    is_active = db.Column(db.Boolean, default=True)

    coach_id = db.Column(db.Integer, db.ForeignKey('coaches.id'))
