from os import path
from flask import Blueprint, render_template, flash, redirect, url_for

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

        human_to_register = Human(first_name=form.first_name.data, last_name=form.last_name.data)
        human_to_register.create(commit=False)

        user_to_register = User(username=form.username.data, email_address=form.email_address.data, phone_number=form.phone_number.data, password=form.password.data, human_id=human_to_register.id)

        user_to_register.create()

        flash("Account registered successfully", "success")
        return redirect(url_for("auth_bp.login_get"))
    else:
        [[flash(error, category="danger") for error in errors] for errors in form.errors.values()]
        return redirect(url_for("auth_bp.register_get", form=form))


# TODO: I should configure login and logout

@auth_bp.route("/login")
def login_get():
    return render_template("login.html")
