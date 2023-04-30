from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_user, logout_user
from sqlalchemy import or_
from src.views.auth.forms import SignupForm, LoginForm
from src.models.user import User

auth_blueprint = Blueprint('auth', __name__, template_folder="templates")


@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        user.create()
    return render_template("auth/register.html", form=form)


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.login.data).first()
        next = request.args.get("next")
        if user and user.check_password(form.password.data):
            login_user(user)
            if next:
                return redirect(next)
            else:
                return redirect(url_for('main.index'))
    return render_template("auth/login.html", form=form)


@auth_blueprint.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.index"))