from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# main sqlalchemy file#

app = Flask(__name__)
projectdir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(projectdir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
