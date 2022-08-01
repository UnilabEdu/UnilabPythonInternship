from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'my_secret_key'
    register_blueprints(app)

    @app.route('/')
    def home():
        return render_template('home.html')

    return app


def register_blueprints(app):
    from src.users.views import users_blueprint
    app.register_blueprint(users_blueprint, url_prefix='/user')

    from src.posts.views import posts_blueprint
    app.register_blueprint(posts_blueprint, url_prefix='/post')

    from src.profiles.views import profiles_blueprint
    app.register_blueprint(profiles_blueprint)
