from flask import Flask

from src.config import Config
from src.extensions import db, login_manager
from src.admin import admin, SecureModelView, SecureIndexView, ProductView, WorkView
from src.views import product_blueprint, main_blueprint, auth_blueprint 
from src.commands import init_db, populate_db
from src.models import User, Product, Contact, Works




COMMANDS = [
    init_db, 
    populate_db
]


BLUEPRINTS = [
    product_blueprint,
    main_blueprint,
    auth_blueprint
]

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extenstions(app)
    register_blueprints(app)
    register_commands(app)


    return app

def register_extenstions(app):
    db.init_app(app)

    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
    
    #flask admin
    admin.init_app(app)
    admin.add_view(ProductView(Product, db.session, name='Products', endpoint="product_admin"))
    admin.add_view(WorkView(User, db.session))
    admin.add_view(SecureModelView(Contact, db.session))
    admin.add_view(SecureModelView(Works, db.session))

def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)   
       


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)


