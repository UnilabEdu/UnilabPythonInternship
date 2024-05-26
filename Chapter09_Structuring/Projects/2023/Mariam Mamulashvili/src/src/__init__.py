from flask import Flask
from src.config import Config
from src.extensions import db


from src.views import product_blueprint, main_blueprint, auth_blueprint 

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extenstions(app)
    app.register_blueprint(product_blueprint)   
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)

    return app

def register_extenstions(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
