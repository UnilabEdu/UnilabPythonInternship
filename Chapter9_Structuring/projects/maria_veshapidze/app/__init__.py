from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = "SecretKey"
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+os.path.join(basedir, "data.sqlite")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


from app.students.views import students_blueprint
from app.tutors.views import tutors_blueprint
from app.common.views import common_blueprint

app.register_blueprint(students_blueprint, url_prefix="/students")
app.register_blueprint(tutors_blueprint, url_prefix="/tutors")
app.register_blueprint(common_blueprint, url_prefix="/common")
