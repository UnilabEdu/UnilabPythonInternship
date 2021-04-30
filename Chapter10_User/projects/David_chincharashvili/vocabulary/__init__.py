import os
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, logout_user, login_user, login_required, UserMixin, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(min=4, max=8)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=4, max=8)])
    email = StringField("Email",  validators=[Email()])


basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# PREPARE OBJECTS
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


class Users(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %s>' % self.username


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile(os.path.join(basedir, 'config.cfg'))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, "data.sqlite")

    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    login_manager.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route('/')
    @login_required
    def home():
        return f"Only Logged in users can see Home Page, so Hello {current_user.username}"

    @app.route("/register")
    def register():
        form = LoginForm()
        if form.validate_on_submit():
            pass


        return render_template('login.html', title="Login", form=form, methods=["POST", "GET"])

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))

    @app.route("/login")
    def login():
        user = Users.query.filter_by(username="David").first()
        print(user)
        login_user(user)
        return "You are logged in"

    @app.route("/logout")
    def logout():
        logout_user()
        return "You logged out successfully"

    return app
