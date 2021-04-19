import json
import requests
import os
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

if __name__ == '__main__':
    app.run(debug=True)
