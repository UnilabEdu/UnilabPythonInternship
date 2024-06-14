from flask import render_template, Blueprint, flash, redirect, url_for, request, session
from flask_login import login_user, logout_user, login_required

from src.views.auth.forms import RegisterForm, LoginForm
from src.config import Config
from src.models.user import User

from os import path


TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "auth")
auth_blueprint = Blueprint("auth", __name__, template_folder=TEMPLATES_FOLDER)


@auth_blueprint.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.repeat_password.data 
        )
        user.role_id = 3
        user.create()

        flash("Registration successful!", "success")
        return redirect(url_for("auth.login"))
    
    if form.errors:
        for errors in form.errors.values():
            for error in errors:
                flash(error)

    return render_template("register.html", form=form)


@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        
        if user and user.check_password(form.password.data):
            login_user(user)
            flash("Login successful!", "success")
            next = request.args.get("next")
            return redirect(next or url_for("main.index"))
        
        else:
            flash("Login unsuccessful. Please check email and password", "danger")
    return render_template("login.html", form=form)

@auth_blueprint.route("/logout")
@login_required
def logout():
    session.pop('quiz_id', None)
    session.pop('selected_questions', None)
    session.pop('current_question', None)
    session.pop('score', None)

    logout_user()
    flash("You have been logged out.", "success")
    return redirect(url_for("auth.login"))