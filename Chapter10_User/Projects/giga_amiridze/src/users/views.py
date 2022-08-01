from flask import Blueprint, render_template
from src.users.forms import Signup, Login

users_blueprint = Blueprint('user',
                           __name__,
                           template_folder='templates/users'
                           )

@users_blueprint.route('/signup')
def signup():
    form = Signup()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        terms_agree = form.terms_agree.data

    return render_template('signup.html', form=form)

@users_blueprint.route('/login')
def login():
    form = Login()

    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
        remember = form.remember.data

    return render_template('login.html', form=form)
