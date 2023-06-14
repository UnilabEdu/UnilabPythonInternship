from flask import Blueprint, render_template, flash, redirect, url_for, request
from os import path
from market.views import RegistrationForm, LoginForm
from market.config import Config
from market.models import User
from flask_login import login_user, logout_user


TEMPALTE_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "auth")
auth_blueprint = Blueprint('auth', __name__, template_folder=TEMPALTE_FOLDER)


@auth_blueprint.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User()
        form.populate_obj(user)
        user.role_id = 2
        user.create()
        login_user(user)

        return redirect(url_for('main.home'))

    return render_template("register.html", form=form)


@auth_blueprint.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            flash("Can't find User")
            return redirect(url_for("auth.login"))
        if user.check_password(form.password.data):
            login_user(user)
            next = request.args.get('next')
            if next:
                return redirect(next)
            else:
                return redirect(url_for("main.home"))
            return redirect(url_for("main.home"))
        else:
            flash("Password is incorrect")
    return render_template("login.html", form=form)


@auth_blueprint.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.home"))



