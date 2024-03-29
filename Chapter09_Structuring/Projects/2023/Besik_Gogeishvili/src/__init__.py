from flask import Flask

from src.config import Config
from src.extensions import db, migrate
from src.views import main, auth, petitions
from src.commands import init_db, populate_db


BLUEPRINTS = [main, auth, petitions]
COMMANDS = [init_db, populate_db]


def create_app():
    
    app = Flask(__name__, template_folder="./templates")
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

    # Flask-Migrate
    migrate.init_app(app, db)


def register_commands(app):

    for command in COMMANDS:
        app.cli.add_command(command)
        