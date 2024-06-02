from flask import Flask

from src.views.admin_views.base import SecureModelView
from src.views.admin_views.products import ProductView
from src.models import Users, Products
from src.ext import db, login_manager, admin,migrate
from src.config import Config
from src.views.auth.routes import auth_bp
from src.views.products.routes import products_bp
from src.views.main.routes import main_bp
from src.command import init_db




BLUEPRINTS = [auth_bp,main_bp,products_bp]
COMMANDS =[init_db]

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
    migrate.init_app(app,db)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.login_message = "გთხოვთ გაიარეთ ავტორიზაცია"

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(user_id)
    

    admin.init_app(app)
    admin.add_view(SecureModelView(Users, db.session, name='Users'))
    admin.add_view(ProductView(Products, db.session, name='admin_products'))

    
    




def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)







