from flask import Flask

from app.extensions import db, migrate, login_manager


def create_app(config_file='config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)


def register_blueprints(app):
    from app.main.views import main_blueprint
    app.register_blueprint(main_blueprint)

    from app.blog.views import blog_blueprint
    app.register_blueprint(blog_blueprint)

    from app.auth.views import auth_blueprint
    app.register_blueprint(auth_blueprint)

