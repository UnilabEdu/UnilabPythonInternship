from flask import Blueprint, render_template, redirect, url_for
from os import path

from src.views.auth.forms import SigninForm, RegisterForm
from src.config import Config


TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "auth")
auth_bp = Blueprint("auth", __name__, template_folder=TEMPLATES_FOLDER)


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect(url_for('sign_in'))
    return render_template('register.html', form=form)


@auth_bp.route('/sign-in', methods=["GET", "POST"])
def sign_in():
    form = SigninForm()
    if form.validate_on_submit():
        print(f"Email: {form.email.data}, Remember me: {form.remember_me.data}")
        return redirect(url_for('home'))
    return render_template('sign_in.html', form=form)