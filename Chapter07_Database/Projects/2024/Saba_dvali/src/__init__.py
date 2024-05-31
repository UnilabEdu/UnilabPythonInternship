from flask import Flask

from src.models import Users
from src.ext import db, login_manager
from src.config import Config
# from src.views.auth.routes import auth_bp
# from src.views.products.routes import products_bp
from src.views.main.routes import main_bp
from src.commands import init_db

# BLUEPRINTS = [ main_bp, products_bp, auth_bp ]
BLUEPRINTS = [ main_bp ]

COMMANDS = [ init_db ]


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    return app


def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)
        

def register_extensions(app):
    
    db.init_app(app)
    
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(user_id)



def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)
