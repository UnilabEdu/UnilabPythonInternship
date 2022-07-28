from flask import Blueprint, render_template, redirect, url_for
from src.users.forms import Signup
from src.models import User

users_blueprint = Blueprint('users',
                            __name__,
                            template_folder='templates/users'
                            )

# server:port/blueprint_prefix/route_name
@users_blueprint.route('/', methods=['GET', 'POST'])
def signup():
    form = Signup()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        conf_pass = form.conf_pass.data
        terms_agree = form.terms_agree.data

        user = User()
        user.create(name=name, email=email, password=password, terms_agree=terms_agree, commit=True)
        return redirect(url_for('public.home'))

    return render_template('signup.html', form=form)
