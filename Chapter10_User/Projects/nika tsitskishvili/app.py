from flask import Flask, render_template, request, url_for, redirect
from flask_login import LoginManager, logout_user,login_required, UserMixin, login_user, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
import os
from forms import RegisterTable
from wtforms import ValidationError
project_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+os.path.join(project_dir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "wekhgjjfjfj"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


class Crud():
    @classmethod
    def create(cls, **kwargs):
        item = cls(**kwargs)
        cls.save(item)
    @classmethod
    def read(cls, **kwargs):
        return cls.query.filter_by(**kwargs).first()
        #cls.query.filter(cls.age >= 2)
    @classmethod
    def update(cls, name, new_name, new_id):
        ob = cls.query.filter_by(name=name).first()
        ob.name = new_name
        if new_id != None:
            ob.writer_id = new_id
        db.session.commit()
    @classmethod
    def delete(cls, name):
        ob = cls.query.filter_by(name=name).first()
        db.session.delete(ob)
        db.session.commit()
    def save(self):
        db.session.add(self)
        db.session.commit()

class User(db.Model,Crud,UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
    def validate_email_from_db(self):
        temp_email = self.email.data
        if User.query.filter_by(email=temp_email).first():
            raise ValidationError("Email already exists")


    def __repr__(self):
        return self.name
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")
@app.route("/data", methods=["GET", "POST"])
@login_required
def data():
    return render_template("forbidden.html")
@app.route("/register", methods=["GET","POST"])
def create():
    regform = RegisterTable()
    if regform.validate_on_submit() and regform.submit.data:
        name = regform.name.data
        email = regform.email.data
        password = regform.password.data
        confirm_password = regform.confirm_password.data
        if password == confirm_password:
            User.create(name=name, email=email, password=generate_password_hash(password))
    else:
        pass
    return render_template("create.html", regform=regform)


@app.route("/login", methods=["GET","POST"])
def login():
    regform = RegisterTable()
    if regform.validate_on_submit() and regform.submit.data:
        email = regform.email.data
        password = regform.password.data
        user = User.query.filter_by(email=email).first()
        if user is not None and check_password_hash(user.password, password):
            login_user(user)
            next = request.args.get('next')
            if next is None:
                next = url_for('home')
            return redirect(next)
    return render_template("login.html", regform=regform)
@app.route("/logout", methods=["GET","POST"])
def logout():
    logout_user()
    return render_template("home.html")
if __name__ == '__main__':
    app.run()