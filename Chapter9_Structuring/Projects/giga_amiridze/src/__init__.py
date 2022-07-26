from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'my_secret_key'
    register_blueprints(app)

    return app

def register_blueprints(app):
    from src.users.views import users_blueprint
    app.register_blueprint(users_blueprint)

    from src.public.views import public_blueprint
    app.register_blueprint(public_blueprint)

    from src.posts.views import posts_blueprint
    app.register_blueprint(posts_blueprint, url_prefix='/post')
