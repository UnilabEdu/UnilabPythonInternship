from flask import render_template, redirect, url_for, Blueprint, flash, request
from flask_login import login_user, logout_user

from src.views.auth.forms import Login, Register
from src.config import Config
from src.models import User

import os


TEMPLATES_FOLDER = os.path.join(Config.BASE_DIRECTORY, "templates", "auth")
auth = Blueprint("auth", __name__, template_folder=TEMPLATES_FOLDER)


@auth.route("/login", methods=["GET", "POST"])
def login():
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
    form = Register()

    if form.validate_on_submit():

        if not User.query.filter(User.username == form.username.data).first():

            user = User()
            form.populate_obj(user)

            user.create()


            return redirect(url_for("main.home"))
        
        else:
            flash("That username is taken. Try another.")

    return render_template("register.html", form=form)


@auth.route("/logout")
def logout():

    logout_user()

    return redirect(url_for("main.home"))