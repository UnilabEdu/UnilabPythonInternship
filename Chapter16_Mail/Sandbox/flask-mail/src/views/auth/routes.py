from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_user, logout_user

from src.views.auth.forms import SignupForm, LoginForm, PasswordRecoveryForm, ResetPasswordForm
from src.models.user import User
from src.emails import create_key, send_email, confirm_key


auth_blueprint = Blueprint('auth', __name__, template_folder="templates")


@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        user.create()

        key = create_key(form.email.data)
        html = render_template('auth/_activation_message.html', key=key)
        send_email("Confirm your account", html, form.email.data)

    return render_template("auth/register.html", form=form)


@auth_blueprint.route("/confirm_email/<string:key>")
def confirm_email(key):
    email = confirm_key(key)
    user = User.query.filter_by(email=email).first()
    if user and not user.confirmed:
        user.confirmed = True
        user.save()
        return redirect(url_for('main.index'))
    else:
        return "Wrong secret key or expired, or already confirmed"


@auth_blueprint.route("/forgot_password", methods=['GET', 'POST'])
def forgot_password():
    form = PasswordRecoveryForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            user.reset_password = True
            reset_key = create_key(form.email.data)
            html = render_template('auth/_reset_message.html', key=reset_key)
            send_email("Reset your password", html, form.email.data)
            user.save()
            return "You have been emailed password reset link"
    return render_template('auth/forgot_password.html', form=form)


@auth_blueprint.route("/reset_password/<string:key>", methods=['GET', 'POST'])
def reset_password(key):
    form = ResetPasswordForm()
    email = confirm_key(key)
    user = User.query.filter_by(email=email).first()

    if not user: return "Wrong secret key or expired, or already confirmed"
    if not user.reset_password: return "Password already reset"

    if form.validate_on_submit():
        user.password = form.password.data
        user.reset_password = False
        user.save()
        return redirect(url_for('auth.login'))
    return render_template("auth/reset_password.html", form=form)


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.login.data).first()
        next = request.args.get("next")
        if user and user.check_password(form.password.data):
            login_user(user)
            if next:
                return redirect(next)
            else:
                return redirect(url_for('main.index'))
    return render_template("auth/login.html", form=form)


@auth_blueprint.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.index"))