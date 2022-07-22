from flask import Flask

from app.extentions import db, migrate, login_manager

def create_app(config_file = 'config.py'):
    application = Flask(__name__)
    application.config.from_pyfile(config_file)
    register_extentions(application)

    register_blueprints(application)
    register_login(application)

    return application

def register_extentions(application):
    db.init_app(application)
    migrate.init_app(application, db)

def register_blueprints(application):
    from app.coaches.views import coaches_blueprint
    application.register_blueprint(coaches_blueprint, url_prefix='/coaches')

    from app.public.views import public_blueprint
    application.register_blueprint(public_blueprint)

    from app.pupils.views import pupils_blueprint
    application.register_blueprint(pupils_blueprint, url_prefix='/pupils')

    from app.user.views import user_blooprint
    application.register_blueprint(user_blooprint, url_prefix='/user')

def register_login(application):
    login_manager.init_app(application)
    login_manager.login_view = "user.login"