from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'my_secret_key'
    register_blueprints(app)

    return app

def register_blueprints(app):
    from src.users.views import users_blueprint
    app.register_blueprint(users_blueprint, url_prefix='/user')
