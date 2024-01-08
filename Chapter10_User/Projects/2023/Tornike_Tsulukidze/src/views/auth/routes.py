from os import path

from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_user, logout_user

from src.config import Config
from src.views.auth.forms import RegisterForm, LoginForm
from src.models import User, Human


TEMPLATE_FOLDER = path.join(Config.TEPMLATE_FOLDER, "auth")
auth_bp = Blueprint("auth_bp", __name__, url_prefix="/auth", template_folder=TEMPLATE_FOLDER)


@auth_bp.get("/register")
def register_get():
    form = RegisterForm()
    return render_template("register.html", form=form)


@auth_bp.post("/register")
def register_post():
    form = RegisterForm()
    if form.validate_on_submit():

        human_to_register = Human(form.first_name.data, form.last_name.data)
        human_to_register.create(commit=False)

        user_to_register = User(form.username.data, form.email_address.data, form.phone_number.data, form.password.data, human_to_register.id, 1)

        user_to_register.create()

        flash("Account registered successfully", "success")
        return redirect(url_for("auth_bp.login_get"))
    else:
        [[flash(error, category="danger") for error in errors] for errors in form.errors.values()]
        return redirect(url_for("auth_bp.register_get", form=form))


@auth_bp.get("/login")
def login_get():
    form = LoginForm()
    return render_template("login.html", form=form)


@auth_bp.post("/login")
def login_post():
    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(email_address=form.email_address.data).first()
        if not user:
            flash("This email address is not registered!", "danger")
            return redirect(url_for("auth_bp.login_get"))

        if not user.check_password(form.password.data):
            flash("Invalid password!", "danger")
            return redirect(url_for("auth_bp.login_get"))

        flash(f"Logged in successfully, as {user.username}", "success")
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for("main_bp.main_get"))
    else:
        [[flash(error, category="danger") for error in errors] for errors in form.errors.values()]
        return redirect(url_for("auth_bp.login_get"))


@auth_bp.route("/logout")
def logout():
    logout_user()
    flash("Logged out.", "success")
    return redirect(url_for("auth_bp.login_get"))
