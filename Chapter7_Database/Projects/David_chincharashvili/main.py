import json
import os
import requests
from flask import Flask, render_template, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, length, Email

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

db_path = "sqlite:///" + os.path.join(basedir, 'data.sqlite')

app.config['SECRET_KEY'] = "this_is_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    location = db.relationship('Location', backref='user', lazy=True, uselist=False)

    def __init__(self, username, email, location):
        self.username = username
        self.email = email
        self.location = location

    def __repr__(self):
        return f"User {self.username} with email: {self.email}"

    @classmethod
    def save(cls, name, email, location):
        user = cls.query.filter_by(email=email).first()
        if user:
            user.username = name
            user.email = email
            user.location = location
        else:
            user = cls(name, email, location)
        db.session.add(user)
        db.session.commit()

    @classmethod
    def rm(cls, email):
        user = cls.query.filter_by(email=email).first()
        db.session.delete(user)
        db.session.commit()

    @classmethod
    def get(cls, email):
        return cls.query.filter_by(email=email).all()


class Location(db.Model):
    __tablename__ = "locations"
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __init__(self, address, user_id):
        self.address = address
        self.user_id = user_id

    def __repr__(self):
        return f"User {self.user_id} at address: {self.address}"

    @classmethod
    def save(cls, str_address, user_id):
        address = cls.query.filter_by(user_id=user_id).first()
        if address:
            address.address = str_address
            address.user_id = user_id
        else:
            address = cls(str_address, user_id)
        db.session.add(address)
        db.session.commit()

    @classmethod
    def rm(cls, user_id):
        address = cls.query.filter_by(user_id=user_id).first()
        db.session.delete(address)
        db.session.commit()

    @classmethod
    def get(cls, user_id):
        return cls.query.filter_by(user_id=user_id).all()


class FormModel(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    textarea = db.Column(db.String)

    def __init__(self, name, email, textarea):
        self.name = name
        self.email = email
        self.textarea = textarea

    @classmethod
    def save(cls, name, email, textarea):
        message = cls.query.filter_by(email=email).first()
        if message:
            message.username = name
            message.email = email
            message.textarea = textarea
        else:
            message = cls(name, email, textarea)
        db.session.add(message)
        db.session.commit()

    @classmethod
    def rm(cls, id):
        message = cls.query.filter_by(id=id).first()
        db.session.delete(message)
        db.session.commit()

    @classmethod
    def get(cls, id):
        return cls.query.filter_by(id=id).first()


class FormName(FlaskForm):
    name = StringField("Name")
    email = StringField("Email", [DataRequired(), length(max=100, min=5), Email("Field should be real Email")])
    textarea = TextAreaField("Message", [DataRequired(), length(min=5)])
    submit = SubmitField("Send")


@app.route('/')
def home():
    return render_template('page.html')


@app.route('/about_us')
def about():
    resp = requests.get("https://jsonplaceholder.typicode.com/users")
    data = json.loads(resp.text)
    return render_template('about.html', data=data)


@app.route('/contact_us', methods=['GET', 'POST'])
def contact():
    form = FormName(request.form)
    if form.validate_on_submit():
        email = form.email.data
        name = form.name.data
        textarea = form.textarea.data
    return render_template('contact.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
