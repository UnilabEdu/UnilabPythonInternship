from flask import Flask
from src.extensions import db, migrate
from src.config import Config
from src.views import main_blueprint, product_blueprint
from src.commands import init_db, populate_db

BLUEPRINTS = [main_blueprint, product_blueprint]
COMMANDS = [init_db, populate_db]


def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)

    return app


def register_extensions(app):

    # Flask-SQLAlchemy
    db.init_app(app)

    # Flask-Migrate
    migrate.init_app(app, db)


def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)