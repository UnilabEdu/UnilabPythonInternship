from flask import Flask

from flask_admin.contrib.sqla import ModelView
from app.models import User, Coach, Pupil
from app.extentions import db, migrate, login_manager, admin
from admin import Userview
from flask_admin.menu import MenuLink



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


    admin.init_app(application)
    admin.add_view(Userview(User, db.session))
    admin.add_view(ModelView(Coach, db.session, category="Coaches and Pupils"))
    admin.add_view(ModelView(Pupil, db.session, category="Coaches and Pupils"))

    admin.add_link(MenuLink(name='return home', url='/'))



def register_blueprints(application):
    from app.coaches.views import coaches_blueprint
    application.register_blueprint(coaches_blueprint, url_prefix='/coaches')

    from app.public.views import public_blueprint
    application.register_blueprint(public_blueprint)

    from app.pupils.views import pupils_blueprint
    application.register_blueprint(pupils_blueprint, url_prefix='/pupils')

    from app.user.views import users_blooprint
    application.register_blueprint(users_blooprint, url_prefix='/users')

def register_login(application):
    login_manager.init_app(application)
    login_manager.login_view = "users.login"