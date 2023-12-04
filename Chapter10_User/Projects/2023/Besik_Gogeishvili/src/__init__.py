from flask import Flask

from src.config import Config
from src.extensions import db, migrate, login_manager
from src.views import main, auth, petitions, user
from src.admin import admin
from src.admin.base import SecureModel
from src.models import User, Petition, Signer
from src.commands import init_db, populate_db

BLUEPRINTS = [main, auth, petitions, user]
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

    # Flask-Migrate
    admin.init_app(app)
    admin.add_view(SecureModel(User, db.session, name="მომხმარებლები", endpoint="users_panel"))
    admin.add_view(SecureModel(Petition, db.session, name="პეტიციები", endpoint="petitions_panel"))
    admin.add_view(SecureModel(Signer, db.session, name="ხელმომწერები", endpoint="signers_panel"))

    # Flask-Login
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)
