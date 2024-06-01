from flask import Flask
from flask_admin.menu import MenuLink

from src.admin_views import SecureModelView, UserView, ProductView
from src.models import User, Product
from src.ext import db, migrate, login_manager, admin
from src.config import Config
from src.views import main_blueprint, product_blueprint, auth_blueprint
from src.commands import init_db, populate_db

BLUEPRINTS = [main_blueprint, product_blueprint, auth_blueprint]
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

    # Flask-Login
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.login_message = "გთხოვთ გაიარეთ ავტორიზაცია"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    # Flask-Admin
    admin.init_app(app)
    admin.add_view(UserView(User, db.session, category="Some Category"))
    admin.add_view(ProductView(Product, db.session, category="Some Category"))

    admin.add_link(MenuLink("", url="/", icon_type="fa", icon_value="fa-sign-out"))


def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)