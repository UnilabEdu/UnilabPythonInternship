from flask import Flask
from flask_admin.menu import MenuLink

from src.extensions import db, migrate, login_manager
from src.admin import admin, SecureModelView, UserView, ProductView
from src.config import Config
from src.models import User, Product, Role, Student, University
from src.views import main_blueprint, product_blueprint, auth_blueprint
from src.commands import init_db_command, populate_db_command

BLUEPRINTS = [main_blueprint, product_blueprint, auth_blueprint]
COMMANDS = [init_db_command, populate_db_command]


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

    # Flask-Admin
    admin.init_app(app)
    admin.add_view(UserView(User, db.session, name="მომხმარებლები", category="მომხმარებლის მართვა"))
    admin.add_view(SecureModelView(Role, db.session, name="როლები", category="მომხმარებლის მართვა"))
    admin.add_view(ProductView(Product, db.session))
    admin.add_view(SecureModelView(University, db.session, category="University Management"))
    admin.add_view(SecureModelView(Student, db.session, category="University Management"))

    admin.add_link(MenuLink("Return", url="/", icon_type="fa", icon_value="fa-sign-out"))

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)


def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)