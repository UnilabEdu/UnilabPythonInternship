from flask import Flask
from melomane.config import Config
from melomane.views.main.routes import main_blueprint
from melomane.views.registration.routes import registration_blueprint
from melomane.extensions import db


BLUEPRINTS = [main_blueprint, registration_blueprint]

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_blueprints(app)
    register_extensions(app)
    return app

def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)

def register_extensions(app):
    db.init_app(app)