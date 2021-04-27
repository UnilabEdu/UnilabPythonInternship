from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = "mySECRETkey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app, db)


class NursesModel(db.Model):
    __tablename__ = "nurses"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    address = db.Column(db.String)
    department = db.Column(db.String)
    shift = db.Column(db.Integer)

    def __init__(self, email, first_name, last_name, address, department, shift):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.department = department
        self.shift = shift

    def __repr__(self):
        return f'Nurse email:{self.email}, name {self.first_name} {self.last_name}, address: {self.address},' \
               f'department: {self.department}, shift: {self.shift}'


from nurse.nurse_registration.views import nurse_blueprint
app.register_blueprint(nurse_blueprint, url_prefix="/")

from nurse.homepage.views import homepage
app.register_blueprint(homepage, url_prefix="/")
