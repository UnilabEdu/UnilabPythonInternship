from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_user
from src.users.forms import Signup, Login
from src.models import User

users_blueprint = Blueprint('user',
                           __name__,
                           template_folder='templates/users'
                           )

@users_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    form = Signup()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        terms_agree = form.terms_agree.data

        user = User(name=name, email=email, password=password, terms_agree=terms_agree)
        user.save_to_db()
        return redirect(url_for('user.login'))

    return render_template('signup.html', form=form)

@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        remember = form.remember.data

        user = User.find_by_email(email)

        if user is not None and user.check_password(password):
            login_user(user)

            next = request.args.get('next')

            if next is None:
                next = url_for('welcome')

            return redirect(next)

    return render_template('login.html', form=form)
