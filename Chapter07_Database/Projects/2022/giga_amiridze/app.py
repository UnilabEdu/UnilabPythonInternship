from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

base_dir = os.path.abspath(os.path.dirname(__file__))
db_name = 'data.sqlite'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, db_name)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
