from flask import render_template, redirect, url_for, flash, Blueprint, request
from app.models import User
from app.user.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user

user_blooprint = Blueprint('user',
                           __name__,
                           template_folder='templates')


@user_blooprint.route('/registration', methods=['GET', 'POST'])
def registration():
    my_form = RegistrationForm()

    if my_form.validate_on_submit():
        user = User(email=my_form.email.data,
                   username=my_form.username.data,
                   password=my_form.password.data)

        user.save()
        flash("Registration went successfully")
        return redirect(url_for('user.login'))

    return render_template('registration.html', form=my_form)

@user_blooprint.route('/login', methods=['GET', 'Post'])
def login():
    my_form = LoginForm()

    if my_form.validate_on_submit():
        user = User.find_by_email(my_form.email.data)

        if user is not None and user.check_password(my_form.password.data):
            login_user(user)

            flash("Login successful")
            next = request.args.get('next')

            if next is None:
                next = url_for('public.home_page')

            return redirect(next)

    return render_template('login.html', form=my_form)