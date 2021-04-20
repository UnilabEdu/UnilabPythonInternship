import os
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))
# extension objects
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = "MySecretKey"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, "data.sqlite")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['CSRF_ENABLED'] = True

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    with app.app_context():
        db.create_all()

    login_manager.login_view = 'user.login'

    from project.user.views import user_blueprint
    app.register_blueprint(user_blueprint)

    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/welcome')
    @login_required
    def welcome():
        return render_template('welcome.html')

    @app.route('/logout')
    def logout():
        logout_user()
        flash("მომხმარებელი გამოვიდა სისტემიდან")
        return redirect(url_for('home'))

    return app
