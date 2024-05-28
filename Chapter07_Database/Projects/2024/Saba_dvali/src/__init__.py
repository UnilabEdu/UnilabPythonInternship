from flask import Flask

from src.ext import db
from src.config import Config
# from src.views.auth.routes import auth_bp
# from src.views.products.routes import products_bp
from src.views.main.routes import main_bp

# BLUEPRINTS = [ main_bp, products_bp, auth_bp ]
BLUEPRINTS = [ main_bp ]



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_blueprints(app)
    # register_extensions(app)
    return app


def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)
        

# def register_extensions(app):
    
#     db.init_app(app)
