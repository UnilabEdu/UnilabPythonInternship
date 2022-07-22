from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
projectdir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = 'randomkey'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(projectdir, 'database.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(24))
    email = db.Column(db.String(48))
    password = db.Column(db.String(48))
    experience = db.Column(db.String(24))
    account_type = db.Column(db.String(24))

    def create(self, commit=None, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        if commit is not None:
            self.save()

    @classmethod
    def read(cls, username):
        cls.query.filter_by(name=username).first()

    def update(self, commit=None, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        if commit is not None:
            self.save()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"User: {self.username}"
