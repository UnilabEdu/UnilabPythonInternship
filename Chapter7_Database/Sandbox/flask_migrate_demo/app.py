from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    email = db.Column(db.String(128))
    age = db.Column(db.Integer(), default=0)

    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def save(self):
        db.session.add(self)
        db.session.commit()


@app.route("/home")
def home():
    new_user = User("Guram", "guram@gmail.com", 21)
    new_user.save()

    return "ok", 200
