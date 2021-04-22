from app import db
from app.resources.format_dob import calculate_age


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
        return f'{self.username.capitalize()}: {self.name_first} {self.name_last}, {self.sex}, born {self.dob} ({self.age} years old). Email and phone: {self.email, self.phone}'


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
        return f'Id:{self.id} Posted by: {self.user_id}, time: {self.time} Content: {self.text, self.media}'
