from flask import Flask
from src.config import Config
from src.views.main.routes import main_blueprint
from src.views.features.routes import features_blueprint
from src.views.pricing.routes import pricing_blueprint
from src.views.users.routes import users_blueprint
from src.views.register.routes import register_blueprint
from src.views.about.routes import about_blueprint
from src.extensions import db
from src.commands import init_db

BLUEPRINTS = [main_blueprint, features_blueprint, pricing_blueprint, users_blueprint, register_blueprint,
              about_blueprint]

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
    db.init_app(app)
    # migrate.init_app(app, db)

def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)