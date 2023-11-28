from flask import Flask

from src.config import Config
from src.extentions import db, migrate, login_manager
from src.views import auth_blueprint, main_blueprint, product_blueprint
from src.commands import init_db, populate_db
from src.models import User, Product, ProductCategory
from src.admin import admin, SecureModelView, SecureIndexView, UserView, ProductView, RequestView
from src.models.request import Request


BLUEPRINTS = [
    auth_blueprint,
    main_blueprint,
    product_blueprint
]

COMMANDS = [
    init_db,
    populate_db
]


def create_app():
    app = Flask(__name__, template_folder="template")
    app.config.from_object(Config)

    register_extension(app)
    register_blueprints(app)
    register_commands(app)

    return app


def register_extension(app):
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
    admin.add_view(ProductView(Product, db.session, endpoint="product_panel", category="Products"))
    admin.add_view(SecureModelView(ProductCategory, db.session, category="Products"))
    admin.add_view(UserView(User, db.session))
    admin.add_view(RequestView(Request, db.session))



def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)


def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)