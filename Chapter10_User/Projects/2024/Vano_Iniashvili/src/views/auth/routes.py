from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_user, logout_user
from os import path

from src.views.auth.forms import SigninForm, RegisterForm
from src.models.user import User
from src.config import Config


TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "auth")
auth_bp = Blueprint("auth", __name__, template_folder=TEMPLATES_FOLDER)


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, password=form.password.data)
        user.create()
        return redirect(url_for('auth.sign_in'))
    return render_template('register.html', form=form)


@auth_bp.route('/sign-in', methods=["GET", "POST"])
def sign_in():
    form = SigninForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data).first()
        next = request.args.get("next")
        if user and user.check_password(form.password.data):
            login_user(user)
            if next:
                return redirect(next)
            else:
                return redirect(url_for('main.home'))
    return render_template('sign_in.html', form=form)


@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.home"))