from flask import Flask, redirect, url_for
from flask_user import UserManager, SQLAlchemyAdapter, current_user
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.menu import MenuLink
from app.config import Config
from app.models.users import User, Role
from app.extensions import db, migrate, admin
from app.views.main.views import main
from app.commands import create_test_user

BLUEPRINTS = [main]
COMMANDS = [create_test_user]


def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    register_commands(app)
    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app):

    # Setup Flask-SQLAlchemy
    db.init_app(app)

    # Setup Flask-Migrate
    migrate.init_app(app, db)

    # Setup Flask-User
    adapter = SQLAlchemyAdapter(db, User)
    UserManager(adapter, app)

    class UserView(ModelView):
        def is_accessible(self):
            return current_user.has_role('Admin')

        def inaccessible_callback(self, name, **kwargs):
            return redirect(url_for('main.home_page'))

        can_create = False
        can_delete = False
        can_edit = True
        column_exclude_list = ['password',]
        column_searchable_list = ['username', 'firstname', 'lastname']
        column_filters = ['country']
        column_editable_list = ['username', 'firstname', 'lastname', 'country', 'roles']
        column_list = ('id', 'username', 'firstname', 'lastname', 'roles')

    #Setup Flask-Admin
    admin.init_app(app)
    admin.add_view(UserView(User, db.session, category="User Management"))
    admin.add_view(ModelView(Role, db.session, category="User Management"))
    admin.add_view(FileAdmin(Config.PROJECT_ROOT + "/static", '/static/', name='Static Files'))

    admin.add_link(MenuLink(name="Return Home", url='/', icon_type="glyph", icon_value="glyphicon-home"))


def register_blueprints(app):

    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)