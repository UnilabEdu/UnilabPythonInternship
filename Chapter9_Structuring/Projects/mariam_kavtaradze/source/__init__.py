from flask import Flask
from source.extensions import db, migrate


def create_app(config_file='config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    from source.user.views import user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/user')
    from source.front.views import base_blueprint
    app.register_blueprint(base_blueprint)



