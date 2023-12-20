from flask import render_template, url_for, redirect, Blueprint
from flask_login import login_user

from src.views.auth.forms import ContactForm, LoginForm
from src.models import User, Contact

from uuid import uuid4


auth_blueprint = Blueprint('auth', __name__)


@auth_blueprint.route('/contact/', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    error_message = None

    if form.validate_on_submit():

        new_message = Contact(name = form.name.data,
                              email = form.email.data,
                                phone = form.phone.data,
                                company = form.company.data,
                                message = form.message.data)
        new_message.create()
        return redirect(url_for('main.home'))
        
    return render_template('auth/contact.html', form=form)


@auth_blueprint.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
        else:
             return render_template('auth/login.html', form=form, error='Invalid username or password')

        print(form.password.data)
        return redirect(url_for('main.home'))
    return render_template('auth/login.html', form=form)


