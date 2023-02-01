from flask import Flask
from .commands import init_db
from .extensions import db, login_manager, migrate
from .models.user import User
from .views.auth.routes import auth
from .views.main.routes import main
from .config import Config

BLUEPRINTS=[main, auth]
COMMANDS=[init_db]

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)

    login_manager.login_view='auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)


    return app


def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)

def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)