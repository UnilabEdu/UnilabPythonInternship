import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from format_dob import calculate_age

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db, render_as_batch=True)


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    name_first = db.Column(db.String)
    name_last = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    phone = db.Column(db.String)
    sex = db.Column(db.String)
    dob = db.Column(db.Date)
    password = db.Column(db.String)
    age = db.Column(db.Integer)
    picture = db.Column(db.String)
    post = db.relationship('PostsModel', backref='usermodel', uselist=False)

    def __init__(self, username, name_first, name_last, email, phone, dob, age, sex, password, picture=None):
        self.username = username
        self.name_first = name_first
        self.name_last = name_last
        self.email = email
        self.phone = phone
        self.dob = dob
        self.sex = sex
        self.password = password
        self.age = calculate_age(dob)
        self.picture = picture

    def __repr__(self):
        if self.page:
            return f'{self.username.capitalize()} owns {self.page}. {self.name_first} {self.name_last}, {self.sex}, aged {self.dob}. Contact: {self.email, self.phone}'
        else:
            return f"{self.username.capitalize()} doesn't own a page. {self.name_first} {self.name_last}, {self.sex}, aged {self.dob}. Contact: {self.email, self.phone}"

    def create(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def read(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


class PostsModel(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime)
    text = db.Column(db.String)
    media = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, time, text=None, media=None, user_id=None):
        self.time = time
        self.text = text
        self.media = media
        self.user_id = user_id

    def __repr__(self):
        return f'Id:{self.id} Posted by: {self.user_id} Content: {self.text, self.media}'

    def create(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def read(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
