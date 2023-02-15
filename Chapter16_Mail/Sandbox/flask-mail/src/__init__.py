from flask import Flask
from src.config import Config
from src.views.main.routes import main_blueprint
from src.views.auth.routes import auth_blueprint
from src.extensions import db, login_manager, mail
from src.commands import init_db, populate_db
from src.models.user import User

BLUEPRINTS = [main_blueprint, auth_blueprint]
COMMANDS = [init_db, populate_db]


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
    mail.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(_id):
        return User.query.get(_id)


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)