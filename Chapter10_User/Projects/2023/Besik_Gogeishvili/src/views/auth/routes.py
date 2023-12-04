from flask import render_template, redirect, url_for, Blueprint, flash, request
from flask_login import login_user, logout_user, current_user

from src.views.auth.forms import Login, Register
from src.config import Config
from src.models import User

import os

TEMPLATES_FOLDER = os.path.join(Config.BASE_DIRECTORY, "templates", "auth")
auth = Blueprint("auth", __name__, template_folder=TEMPLATES_FOLDER)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.error", code="403"))

    form = Login()

    next_page = request.args.get("next")

    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()

        if user and user.check_password_hash(form.password.data):
            login_user(user)

            if next_page:
                return redirect(next_page)

            return redirect(url_for("main.home"))
        else:
            flash("Invalid Password or Username")

    return render_template("login.html", form=form)


@auth.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.error", code="403"))

    form = Register()

    add_on = request.args.get("hidden")

    if form.validate_on_submit():

        if not User.query.filter(User.username == form.username.data).first():

            user = User()
            form.populate_obj(user)
            user.role_id = 2  # Normal User

            if add_on == "secret_key_to_create_admin_profile":
                user.role_id = 1  # Administrator

            user.create()

            # Automatically log in user.
            user = User.query.filter(User.username == form.username.data).first()
            login_user(user)

            return redirect(url_for("main.home"))

        else:
            flash("That username is taken. Try another.")

    return render_template("register.html", form=form)


@auth.route("/logout")
def logout():
    logout_user()

    return redirect(url_for("main.home"))
