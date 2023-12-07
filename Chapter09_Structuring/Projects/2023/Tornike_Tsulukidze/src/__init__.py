from flask import Flask

from src.config import Config
from src.views import main_bp, auth_bp, library_bp
from src.models import db
from src.commands import init_db


BLUEPRINTS = [main_bp, auth_bp, library_bp]
COMMANDS = [init_db]


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_blueprints(app)
    register_extensions(app)
    register_commands(app)

    return app

def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)


def register_extensions(app):

    # Flask-SQLAlchemy
    db.init_app(app)


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)
