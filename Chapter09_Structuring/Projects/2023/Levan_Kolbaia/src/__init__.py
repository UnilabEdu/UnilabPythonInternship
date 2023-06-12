from flask import Flask
from src.extension import db, migrate
from src.config import Config
from src.commands import init_db

BLUEPRINTS = [main_blueprint,cards_blueprint,carbs_blueprint]
COMMANDS = [init_db]

def create_app():

    app = Flask(__name__)
    app.config_from_object(Config)

    register_extension(app)
    register_blueprints(app)
    register_commands(app)

    return app

def register_extension(app):
    db.init_app(app)

    migrate.init_app(app,db)

def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)


def register_commands(app):
    for command in COMMANDS:
        app.cli.register_command(command)

