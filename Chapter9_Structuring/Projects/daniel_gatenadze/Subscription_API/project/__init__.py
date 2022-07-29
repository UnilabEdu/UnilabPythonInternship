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
<<<<<<< HEAD
    from Chapter9_Structuring.Projects.daniel_gatenadze.Subscription_API.project.users.views import signup_blueprint, login_blueprint
    from Chapter9_Structuring.Projects.daniel_gatenadze.Subscription_API.project.webpages.views import webpages_blueprint

    app.register_blueprint(signup_blueprint, url_prefix="/register")
    app.register_blueprint(login_blueprint, url_prefix="/login")
=======
    from users.views import user_blueprint
    from webpages.views import webpages_blueprint

    app.register_blueprint(user_blueprint, url_prefix="/")
>>>>>>> 006c38a55d9efd513647d67423cfcce4c77d895a
    app.register_blueprint(webpages_blueprint)
