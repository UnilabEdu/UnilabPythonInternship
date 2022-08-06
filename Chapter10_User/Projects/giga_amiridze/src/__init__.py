from flask import Flask, render_template
from flask_login import login_required
from src.config import Config
from src.extensions import db, migrate, login_manager
from src.resources.pages import pages

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    register_blueprints(app)

    login_manager.login_view = 'user.login'

    @app.route('/')
    def home():
        return render_template('home.html', pages=pages)

    @app.route('/welcome')
    @login_required
    def welcome():
        return render_template('welcome.html')

    return app

def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

def register_blueprints(app):
    from src.users.views import users_blueprint
    app.register_blueprint(users_blueprint, url_prefix='/user')

    from src.posts.views import posts_blueprint
    app.register_blueprint(posts_blueprint, url_prefix='/post')

    from src.profiles.views import profiles_blueprint
    app.register_blueprint(profiles_blueprint)
