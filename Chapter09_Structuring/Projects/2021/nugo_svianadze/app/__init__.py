from flask import Flask
from app.extensions import db, migrate, login_manager

def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('config.py')

    register_extensions(app)
    register_blueprints(app)

    return app

def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'login'



def register_blueprints(application):
    from app.views import users_blueprint
    application.register_blueprint(users_blueprint, url_prefix='/users')

