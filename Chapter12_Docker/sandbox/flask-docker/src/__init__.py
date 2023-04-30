from flask import Flask
from src.config import Config
from src.views.main.routes import main_blueprint
from src.views.products.routes import products_blueprint
from src.views.actors.routes import actors_blueprint
from src.views.teachers.routes import teachers_blueprint
from src.views.auth.routes import auth_blueprint
from src.extensions import db, migrate, login_manager, admin
from src.commands import init_db_command, populate_db_command
from src.models.user import User

from src.admin.models import SecureModelView, SecureAdminView, ProductModelView, UserModelView
from src.models.product import Product, ProductCategory

from flask_admin.base import MenuLink

BLUEPRINTS = [main_blueprint, products_blueprint, actors_blueprint, teachers_blueprint, auth_blueprint]
COMMANDS = [init_db_command, populate_db_command]


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
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(_id):
        return User.query.get(_id)

    admin.init_app(app)
    admin.add_view(ProductModelView(Product, db.session, endpoint="products", category="Product"))
    admin.add_view(SecureModelView(ProductCategory, db.session, category="Product"))
    admin.add_view(UserModelView(User, db.session))
    admin.add_link(MenuLink("Return", url="/", icon_type="fa", icon_value="fa-sign-out"))


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)