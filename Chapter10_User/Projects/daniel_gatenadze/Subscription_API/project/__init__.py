from flask import Flask
from .config import ConfigMain
from .user.models import User, Role, UserRoles
from .extensions import db, login_manager, admin, migrate
from flask_admin.menu import MenuLink
from .admin_models.admin import UserView, RoleView, StaticView, UserRoleView


def create_app():
    application = Flask(__name__)
    application.config.from_object(ConfigMain)
    register_extension(application)
    register_blueprints(application)
    return application


def register_extension(application):
    db.init_app(application)
    migrate.init_app(application, db)
    login_manager.init_app(application)
    admin.init_app(application)
    admin.add_view(UserView(User, db.session, category='User Management'))
    admin.add_view(RoleView(Role, db.session, category='User Management'))
    admin.add_view(UserRoleView(UserRoles, db.session, category='User Management'))
    admin.add_link(MenuLink(name='Dashboard', url='/'))
    admin.add_view(StaticView(ConfigMain.projectdir + '/static', '/static', name='Static Files'))


def register_blueprints(application):
    from project.user.views import auth_blueprint
    from project.webpages.views import \
        webpages_blueprint

    application.register_blueprint(auth_blueprint)
    application.register_blueprint(webpages_blueprint)

