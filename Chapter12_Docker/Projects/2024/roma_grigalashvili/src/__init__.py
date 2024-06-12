from flask import Flask
from flask_admin.menu import MenuLink

from src.admin import QuestionView, UserView, QuizView
from src.extensions import db, migrate, login_manager, admin
from src.config import Config
from src.commands import init_db_command, populate_db_command
from src.views import main_blueprint, question_blueprint, auth_blueprint, profile_blueprint, game_blueprint
from src.models import User, Question, Quiz


BLUEPRINTS = [main_blueprint, question_blueprint, auth_blueprint, profile_blueprint, game_blueprint]
COMMANDS = [init_db_command, populate_db_command]

def create_app(config=Config):

    app = Flask(__name__)
    app.config.from_object(config)

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)


    return app


def register_extensions(app):

    # Flask-SQLAlchemy
    db.init_app(app)

    # Flask-Migrate
    migrate.init_app(app, db)

    # Flask-Login
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.login_message = 'First of all please Login website.'
    login_manager.login_message_category = "danger"

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))
    
    # Flask-Admin
    admin.init_app(app)
    admin.add_view(UserView(User, db.session))
    admin.add_view(QuestionView(Question, db.session))
    admin.add_view(QuizView(Quiz, db.session))

    admin.add_link(MenuLink("Return", url="/", icon_type="fa", icon_value="fa-sign-out"))

def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)