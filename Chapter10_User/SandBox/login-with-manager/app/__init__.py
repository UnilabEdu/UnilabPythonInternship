import os

from flask import Flask
from flask_migrate import Migrate

from app.database import db
from app.models import RandomModel


# app = Flask(__name__)

migrate = Migrate()


def create_app():
    # Create a Flask application.

    # Instantiate Flask
    app = Flask(__name__)

    # Load App Config settings
    app.config['SECRET_KEY'] = 'mysecretkey'
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Setup Flask-SQLAlchemy
    db.init_app(app)

    # Setup Flask-Migrate
    migrate.init_app(app, db, render_as_batch=True)

    return app
