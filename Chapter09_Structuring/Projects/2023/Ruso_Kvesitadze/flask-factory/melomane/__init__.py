from flask import Flask
from melomane.config import Config
from melomane.views.main.routes import main_blueprint
from melomane.views.registration.routes import registration_blueprint
from melomane.commands import init_db
from melomane.extensions import db, migrate



BLUEPRINTS = [ main_blueprint, registration_blueprint]

COMMANDS = [init_db ]

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
    db.init_app(app)
    migrate.init_app(app, db)


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)