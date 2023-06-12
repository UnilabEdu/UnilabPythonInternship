from market.config import Config
from market.extensions import db, migrate, login_manager
from flask import Flask
from market.models import User, Product, Role
from market.views import product_blueprint, main_blueprint, auth_blueprint, profile_blueprint
from market.commands import init_db, populate_db
from market.admin import admin, SecureModelView
from flask_admin.menu import MenuLink

BLUEPRINTS = [main_blueprint, product_blueprint, auth_blueprint, profile_blueprint]
COMMANDS = [init_db, populate_db]


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_commands(app)
    register_blueprints(app)

    return app


def register_extensions(app):
    # Flask-SQLAlchemy
    db.init_app(app)

    # Flask-Migrate
    migrate.init_app(app, db)

    # Flask-Login
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    # Flask-Admin
    admin.init_app(app)
    admin.add_view(SecureModelView(Product, db.session))
    admin.add_view(SecureModelView(User, db.session))
    admin.add_view(SecureModelView(Role, db.session))

    admin.add_link(MenuLink("Return", url="/"))


def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)
