import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db, render_as_batch=True)


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    full_name = db.Column(db.String)
    email = db.Column(db.String)
    age = db.Column(db.Integer)
    sex = db.Column(db.String)
    phone = db.Column(db.String)
    page = db.relationship('PagesModel', backref='usermodel', uselist=False)

    def __init__(self, username, full_name, email, age, sex, phone):
        self.username = username
        self.full_name = full_name
        self.email = email
        self.age = age
        self.sex = sex
        self.phone = phone

    def __repr__(self):
        if self.page:
            return f'{self.username} owns {self.page}. {self.full_name}, {self.sex}, aged {self.age}. Contact: {self.email, self.phone}'
        else:
            return f"{self.username} doesn't own a page. {self.full_name}, {self.sex}, aged {self.age}. Contact: {self.email, self.phone}"


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


class PagesModel(db.Model):
    __tablename__ = 'pages'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    followers = db.Column(db.Integer)
    topic = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, title, followers, topic, user_id=None):
        self.title = title
        self.followers = followers
        self.topic = topic
        self.user_id = user_id

    def __repr__(self):
        return f'{self.title} with {self.followers} followers. Topic: {self.topic}'

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
