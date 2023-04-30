import os
from flask import Flask, render_template, redirect, url_for, flash, request, session
from flask_login import LoginManager, logout_user, login_user, login_required, UserMixin, current_user
from werkzeug.security import generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(min=4, max=8)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=4, max=8)])
    email = StringField("Email", validators=[Email()])


basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# PREPARE OBJECTS
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
admin = Admin()


class Users(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    words = db.relationship('Words', backref="users", lazy="dynamic")

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %s>' % self.username


class Words(db.Model):
    __tablename__ = "words"
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String, unique=True)
    hint = db.Column(db.String)
    assoc = db.Column(db.String)
    translation = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return "<Words %s - %s>" % (self.word, self.translation)


class UserView(ModelView):
    # column_exclude_list = ['password']
    # column_display_pk = True
    # def on_model_change(self, form, model, is_created):
    #     model.password = generate_password_hash(model.password, method="sha256")
    pass

class WordsView(ModelView):
    can_export = True




def create_app():
    app = Flask(__name__)
    app.config.from_pyfile(os.path.join(basedir, 'config.cfg'))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, "data.sqlite")
    app.config['USE_SESSION_FOR_NEXT'] = True

    db.init_app(app)
    admin.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    login_manager.login_message = 'You can\'t access that page. You need to login first.'

    admin.add_view(UserView(Users, db.session))
    admin.add_view(WordsView(Words, db.session))

    with app.app_context():
        db.create_all()

    # CONTROLLER

    @login_manager.unauthorized_handler
    def unauthorized_callback():
        return redirect('/login?next=' + request.path)

    @app.route('/')
    @app.route('/home')
    @login_required
    def home():
        return f"Only Logged in users can see Home Page, so Hello {current_user.username}"

    @app.route("/register", methods=["POST", "GET"])
    def register():
        if request.method == "POST":
            pass
        form = LoginForm()
        if form.validate_on_submit():
            pass
        return render_template('login.html', title="Register", form=form)

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            username = request.form['username']
            password = request.form['password']

            user = Users.query.filter_by(username=username).first()
            if not user:
                return "User does not exists!"
            # TODO: add password check to user
            login_user(user)

            # TODO: redirect to dashboard

            if "next" in session:
                return redirect(session['next'])
            return "You are logged in %s" % session['next']

        else:
            if request.args.get("next") is not None:
                print('args has next')
                session["next"] = request.args.get("next")

            print(request.args)
            form = LoginForm()
            if form.validate_on_submit():
                pass
            return render_template('login.html', title="Login", form=form)

    @app.route("/logout")
    def logout():
        logout_user()
        return "You logged out successfully"

    return app
