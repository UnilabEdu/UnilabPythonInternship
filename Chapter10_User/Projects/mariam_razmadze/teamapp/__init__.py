from flask import Flask
from .commands import init_db_command,   populate_db_command
from .extensions import db, login_manager, migrate, admin
from .models.user import User, Role
from .models.question import Question
from .views.auth.routes import auth
from .views.main.routes import main
from .config import Config

from teamapp.admin.models import UserModelView, QuestionModelView, RoleModelView
from flask_admin.base import MenuLink

BLUEPRINTS=[main, auth]
COMMANDS=[init_db_command, populate_db_command]

def create_app():
    app=Flask(__name__)
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
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view='auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
    


    admin.init_app(app)
    admin.add_view(UserModelView(User, db.session))
    admin.add_view(QuestionModelView(Question, db.session))
    admin.add_view(RoleModelView(Role, db.session))
    admin.add_link(MenuLink("Go back", url='/', icon_type='fa', icon_value='fa-sign-out'))


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)