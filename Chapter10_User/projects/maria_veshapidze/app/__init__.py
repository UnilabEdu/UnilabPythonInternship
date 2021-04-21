import os
from flask import Flask, render_template, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, logout_user
from app.pages_list import nav_bar_pages_list


basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = "SecretKey"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir, "data.sqlite")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['CSRF_ENABLED'] = True

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    login_manager.login_view = 'user.login'
    with app.app_context():
        db.create_all()

    from app.students.views import students_blueprint
    from app.tutors.views import tutors_blueprint
    from app.common.views import common_blueprint

    app.register_blueprint(students_blueprint, url_prefix="/students")
    app.register_blueprint(tutors_blueprint, url_prefix="/tutors")
    app.register_blueprint(common_blueprint, url_prefix="/common")

    @app.route('/')
    @app.route('/<guestname>')
    def home(guestname=None):
        return render_template("home_page.html", name=guestname, pages=nav_bar_pages_list)

    @app.route('/about_us')
    def about():
        return render_template("about_us.html", pages=nav_bar_pages_list)

    @app.route('/contact_info')
    def contact():
        return render_template("contact_info.html", pages=nav_bar_pages_list)

    @app.route('/logout')
    def logout():
        logout_user()
        flash("User was logged out")
        return redirect(url_for('home'))

    return app
