from flask import Flask
import runpy
from Chapter9_Structuring.Projects.daniel_gatenadze.Subscription_API.project.extensions import db
from Chapter9_Structuring.Projects.daniel_gatenadze.Subscription_API.project.config import ConfigMain


def create_app():
    app = Flask(__name__)
    app.config.from_object(ConfigMain)

    db.init_app(app)

    # @app.before_first_request
    # def run_populate():
    #     runpy.run_module('Chapter9_Structuring/Projects/daniel_gatenadze/Subscription_API/project/populate')
    '''
             ^ - this is not working yet
    '''

    from Chapter9_Structuring.Projects.daniel_gatenadze.Subscription_API.project.users.views import user_blueprint
    from Chapter9_Structuring.Projects.daniel_gatenadze.Subscription_API.project.webpages.views import webpages_blueprint

    app.register_blueprint(user_blueprint, url_prefix="/")
    app.register_blueprint(webpages_blueprint)

    return app
