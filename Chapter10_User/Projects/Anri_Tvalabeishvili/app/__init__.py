from flask import Flask
from app.config import Config
from app.extensions import db, migrate, login_manager
from app.commands import init_db, populate_db
from app.models.user import User

from app.views.main.routes import main_blueprint
from app.views.Login_Signup.routes import reg_auto_blueprint
from app.views.Game_content.routes import Game_content_blueprint
from app.views.Gift_content.routes import Gift_content_blueprint
from app.views.Admin.routes import Admin_content_blueprint


BLUEPRINTS = [main_blueprint, reg_auto_blueprint, Game_content_blueprint, Gift_content_blueprint, Admin_content_blueprint]
COMMANDS = [init_db, populate_db]


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_blueprints(app)
    register_extensions(app)
    register_commands(app)
    
    return app







def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(_id):
        return User.query.get(_id)


def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)

def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)