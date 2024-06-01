from flask import render_template, Blueprint, flash, redirect, url_for

from src.views.auth.forms import RegisterForm, LoginForm
from src.config import Config

from os import path


TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "auth")
auth_blueprint = Blueprint("auth", __name__, template_folder=TEMPLATES_FOLDER)

users_list = []

@auth_blueprint.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = {
            "username": form.username.data,
            "email": form.email.data,
            "password": form.repeat_password.data
        }
        users_list.append(new_user)
        
        flash("Registration successful!", "success")
        print(users_list)
        return redirect(url_for("auth.login"))
    return render_template("register.html", form=form)


@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = next((u for u in users_list if u["email"] == form.email.data), None)
        if user and user["password"] == form.password.data:
            flash("Login successful!", "success")
            return redirect(url_for("auth.index"))
        else:
            flash("Login unsuccessful. Please check email and password", "danger")
    return render_template("login.html", form=form)