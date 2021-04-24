import os

from flask import Flask
from flask_migrate import Migrate
from flask_user import UserManager, SQLAlchemyAdapter

from app.database import db
from app.models import RandomModel
from app.models.users import User, Role, UserRoles
from app.user.admin import admin

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
    app.config['USER_ENABLE_EMAIL'] = False

    # Setup Flask-SQLAlchemy
    db.init_app(app)

    # Setup Flask-Migrate
    migrate.init_app(app, db, render_as_batch=True)

    # Setup Flask-Admin
    admin.init_app(app)

    # Setup Flask-User
    db_adapter = SQLAlchemyAdapter(db, User)  # Setup the SQLAlchemy DB Adapter
    UserManager(db_adapter, app)  # Init Flask-User and bind to app

    return app
