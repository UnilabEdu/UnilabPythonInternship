from flask import Flask
from flask_admin.menu import MenuLink
from src.config import Config
from src.extensions import db, migrate, login_manager
from src.models import User, Product, Role, Student, University
from src.views import main_blueprint, auth_blueprint, product_blueprint
from src.commands import init_db, populate_db
from src.admin import admin, SecureModelView, UserView, ProductView
from flask_admin.contrib.sqla import ModelView



BLUEPRINTS = [main_blueprint, auth_blueprint, product_blueprint]
COMMANDS = [init_db, populate_db]
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    admin.init_app(app)
    admin.add_view(UserView(User, db.session))
    admin.add_view(ProductView(Product, db.session))
    admin.add_view(SecureModelView(Role, db.session))

    admin.add_link(MenuLink("Return", url="/"))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)

def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)



