from flask import render_template, redirect, url_for, Blueprint

from src.views.auth.forms import Login, Register
from src.config import Config

import os


TEMPLATES_FOLDER = os.path.join(Config.BASE_DIRECTORY, "templates", "auth")
auth = Blueprint("auth", __name__, template_folder=TEMPLATES_FOLDER)


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = Login()

    if form.validate_on_submit():
        print("passed")
        return redirect(url_for("main.home"))

    return render_template("login.html", form=form)


@auth.route("/register", methods=["GET", "POST"])
def register():
    form = Register()

    if form.validate_on_submit():
        print("passed")
        return redirect(url_for("main.home"))

    return render_template("register.html", form=form)