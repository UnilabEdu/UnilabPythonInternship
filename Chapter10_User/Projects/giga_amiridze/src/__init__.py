from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'my_secret_key'
    register_blueprints(app)

    @app.route('/')
    def home():
        return render_template('base.html')

    return app


def register_blueprints(app):
    from src.users.views import user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/user')
