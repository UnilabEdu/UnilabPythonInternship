import os
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# ფლასკის ობიექტი
app = Flask(__name__)
# კონფიგურაცია ფორმისთვის (არამხოლოდ)
app.config['SECRET_KEY'] = "BestKeptSecret"

# კონფიგურაცია მონაცემთა ბაზისთვის
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "data.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

from app.students.views import students_blueprint
app.register_blueprint(students_blueprint, url_prefix="/students")