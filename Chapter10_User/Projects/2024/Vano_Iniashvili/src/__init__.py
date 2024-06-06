from flask import Flask
from src.extensions import db, migrate, login_manager
from src.views.auth.routes import auth_bp
from src.views.films.routes import film_bp
from src.views.main.routes import main_bp
from src.config import Config
from src.commands import init_db
from src.models.user import User

BLUEPRINTS = [main_bp, film_bp, auth_bp]
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
    migrate.init_app(app, db)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(_id):
        return User.query.get(_id)


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)
