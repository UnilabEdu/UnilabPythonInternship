from flask import render_template, Blueprint, redirect, url_for, request
from flask_login import login_user, logout_user

from src.views.auth.forms import RegisterForm, LoginForm
from src.models import User



auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        user.create()
        return redirect(url_for('main.home'))

    return render_template('auth/register.html', form=form)


@auth_blueprint.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next = request.args.get("next", None)
            if next:
                return redirect(next)

        return redirect(url_for('main.home'))

    return render_template('auth/login.html', form=form)




@auth_blueprint.route('/logout', methods=["GET", "POST"])
def logout():
    logout_user()
    return redirect(url_for('main.home'))
