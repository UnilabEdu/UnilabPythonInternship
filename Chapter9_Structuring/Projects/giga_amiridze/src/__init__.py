from flask import Flask
from src.config import Config
from src.extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    register_blueprints(app)
    
    return app

def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)

def register_blueprints(app):
    from src.users.views import users_blueprint
    app.register_blueprint(users_blueprint)

    from src.public.views import public_blueprint
    app.register_blueprint(public_blueprint)

    from src.posts.views import posts_blueprint
    app.register_blueprint(posts_blueprint, url_prefix='/post')
