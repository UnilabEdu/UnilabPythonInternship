from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user
from os import path

from src.config import Config
from src.views.auth.forms import RegisterForm, LoginForm, ResendKeyForm
from src.models import User
from src.utils import send_email, create_key, confirm_key

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

        activation_key = create_key(form.email.data)
        html = render_template("_activation_message.html", activation_key=activation_key)
        send_email("რეგისტრაცია საიტზე", html, [form.email.data])
        flash("აქტივაციის ლინკი გამოგზავნილია")
        return redirect(url_for("main.index"))

    if form.errors:
        for errors in form.errors.values():
            for error in errors:
                flash(error)

    return render_template("register.html", form=form)


@auth_blueprint.route("/resend_key", methods=["GET", "POST"])
def resend_key():
    form = ResendKeyForm()
    if form.validate_on_submit():
        activation_key = create_key(form.email.data)
        html = render_template("_resend_key_message.html", activation_key=activation_key)
        send_email("მეილის აქტივაცია", html, [form.email.data])

        flash("* აქტივაციის კოდი გამოგზავნილია")
        return redirect(url_for("main.index"))

    if form.errors:
        for errors in form.errors.values():
            for error in errors:
                flash(error)

    return render_template("resend_key.html", form=form)


@auth_blueprint.route("/confirm_email/<activation_key>")
def confirm_email(activation_key):

    email = confirm_key(activation_key)
    if not email:
        flash("* აქტივაციის კოდი არ არის სწორი, ან გაუვიდა ვადა")
        return redirect(url_for("auth.register"))

    user = User.query.filter_by(email=email).first()
    if user.confirmed:
        flash("* მომხმარებელი უკვე გააქტიურებულია")
        return redirect(url_for("auth.login"))

    user.confirmed = True
    user.save()
    login_user(user)
    return redirect(url_for("main.index"))


@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            flash("ეს მომხმარებელი ვერ მოიძებნა")
            return redirect(url_for("auth.login"))

        if not user.confirmed:
            flash("თქვენი მეილი არ არის დადასტურებული")
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
