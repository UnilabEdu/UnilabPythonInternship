from flask import Flask
from src.config import Config
from src.extensions import db, migrate
from src.api import api
from src.commands import init_db, populate_db, send_request
from src.models.product import Product, ProductCategory


COMMANDS = [init_db, populate_db, send_request]


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # register_blueprints(app)
    register_extensions(app)
    register_commands(app)

    return app


# def register_blueprints(app):
#     for blueprint in BLUEPRINTS:
#         app.register_blueprint(blueprint)


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)