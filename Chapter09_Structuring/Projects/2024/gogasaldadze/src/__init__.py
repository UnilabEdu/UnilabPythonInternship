from flask import Flask
from src.ext import db
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




def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)







