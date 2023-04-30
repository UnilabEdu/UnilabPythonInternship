from flask import Flask

from app.config import Config
from app.models.user import User
from app.commands import init_db_command, populate_movies_command
from app.ext import db, migrate, login_manager
from app.api import api
from app.views.main.views import main
from app.views.auth.views import auth
from app.views.profile.views import profile

BLUEPRINTS = [main, auth, profile]
COMMANDS = [init_db_command, populate_movies_command]


def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    register_commands(app)
    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app):

    # Setup Flask-SQLAlchemy
    db.init_app(app)

    # Setup Flask-Migrate
    migrate.init_app(app, db)

    #Flask-RESTful
    api.init_app(app)

    # Flask-Login
    @login_manager.user_loader
    def load_user(id_):
        return User.query.get(id_)

    login_manager.init_app(app)


def register_blueprints(app):

    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)
