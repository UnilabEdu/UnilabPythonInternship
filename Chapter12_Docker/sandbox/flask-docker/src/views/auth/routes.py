from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user
from os import path

from src.config import Config
from src.views.auth.forms import RegisterForm, LoginForm
from src.models import User

TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "auth")
auth_blueprint = Blueprint("auth", __name__, template_folder=TEMPLATES_FOLDER)


@auth_blueprint.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User()
        form.populate_obj(user)
        user.role_id = 3
        user.create()

    if form.errors:
        for errors in form.errors.values():
            for error in errors:
                flash(error)

    return render_template("register.html", form=form)


@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            flash("ეს მომხმარებელი ვერ მოიძებნა")
            return redirect(url_for("auth.login"))

        if user.check_password(form.password.data):
            login_user(user)
            next = request.args.get("next")
            if next:
                return redirect(next)
            else:
                return redirect(url_for("main.index"))
        else:
            flash("პაროლი არასწორია")
    return render_template("login.html", form=form)


@auth_blueprint.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.index"))
