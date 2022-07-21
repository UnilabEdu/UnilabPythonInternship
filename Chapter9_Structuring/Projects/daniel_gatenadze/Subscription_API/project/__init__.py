from flask import Flask
import runpy
from Chapter9_Structuring.Projects.daniel_gatenadze.Subscription_API.project.extensions import db
from Chapter9_Structuring.Projects.daniel_gatenadze.Subscription_API.project.config import ConfigMain


def create_app():
    app = Flask(__name__)
    app.config.from_object(ConfigMain)
    register_extension(app)
    register_blueprints(app)
    return app


def register_extension(app):
    db.init_app(app)
    # migrate.init_app(app,db)


def register_blueprints(app):
    from users.views import user_blueprint
    from webpages.views import webpages_blueprint

    app.register_blueprint(user_blueprint, url_prefix="/")
    app.register_blueprint(webpages_blueprint)
