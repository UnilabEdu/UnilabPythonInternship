from flask import Flask
from app.config import test_config
from app.extentions import db, migrate

def create_app(config_file = 'config.py'):
    application = Flask(__name__)
    application.config.from_object(test_config)
    register_extentions(application)

    register_blueprints(application)

    return application

def register_extentions(application):
    db.init_app(application)
    migrate.init_app(application)

def register_blueprints(application):
    from app.coaches.views import coaches_blueprint
    application.register_blueprint(coaches_blueprint, url_prefix='/coaches')

    from app.public.views import public_blueprint
    application.register_blueprint(public_blueprint)
