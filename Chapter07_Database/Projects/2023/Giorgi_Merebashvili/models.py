from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'DshdYAGDASNDUAY7D8DABDAGSDjhdajhd7ada'
app.config['TRACK_DATABASE_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Registrant(db.Model):
    __tablename__ = 'registrants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    sport = db.Column(db.String)