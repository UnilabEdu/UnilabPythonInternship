from flask import Blueprint, redirect, url_for, render_template
from app.models import RegisteredUsers
from app.registration.forms import RegisterForm

registration_blueprint = Blueprint('register',
                                   __name__,
                                   template_folder='templates/registration'
                                   )

@registration_blueprint.route('/register', methods=['GET', 'POST'])
def register():

    form = RegisterForm
    if form.validate_on_submit():
        name = form.name.data
        last_name = form.last_name.data
        email = form.email.data
        password = form.password.data
        user = RegisteredUsers(name,last_name,email,password)
        if user.read(email):
            return "Account with this email already exists"
        else:
            return user.add()
        redirect(url_for())
    return render_template('registration.html', form=form)