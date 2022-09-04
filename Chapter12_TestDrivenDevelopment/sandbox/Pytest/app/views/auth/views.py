from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_user, login_required, logout_user
from app.views.auth.forms import LoginForm, SignupForm
from app.models.user import User

auth = Blueprint('auth', __name__, template_folder='templates')


@auth.route('/register', methods=['GET', 'POST'])
def sign_up():
    form = SignupForm()

    if form.validate_on_submit():
        user = User(form.username.data, form.email.data, form.password.data)
        user.create(commit=True)
        return redirect(url_for('main.home_page'))

    return render_template('auth/register.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.login.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('main.home_page'))

    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home_page'))