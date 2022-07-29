from flask import Flask
from Chapter10_User.Projects.daniel_gatenadze.Subscription_API.project.extensions import db, login_manager
from Chapter10_User.Projects.daniel_gatenadze.Subscription_API.project.config import ConfigMain


def create_app():
    app = Flask(__name__)
    app.config.from_object(ConfigMain)
    register_extension(app)
    register_blueprints(app)
    return app


def register_extension(app):
    db.init_app(app)
    login_manager.init_app(app)


def register_blueprints(app):
    from Chapter10_User.Projects.daniel_gatenadze.Subscription_API.project.users.views import auth_blueprint
    from Chapter10_User.Projects.daniel_gatenadze.Subscription_API.project.webpages.views import \
        webpages_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(webpages_blueprint)
