from flask import Blueprint, render_template, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from Chapter9_Structuring.Projects.daniel_gatenadze.Subscription_API.project.users.forms import RegisterForm, LoginForm
from Chapter9_Structuring.Projects.daniel_gatenadze.Subscription_API.project.users.models import User
from Chapter9_Structuring.Projects.daniel_gatenadze.Subscription_API.project.extensions import BaseModel

user_blueprint = Blueprint('users',
                           __name__,
                           template_folder='templates/students')


@user_blueprint.route('/register')
@user_blueprint.route('/register', methods=['GET', 'POST'])
def sign_up():

    myform = RegisterForm()

    if myform.validate_on_submit():
        hashed_password = generate_password_hash(myform.password.data, method='sha256')
        register = User(username=myform.username.data, email=myform.email.data, password=hashed_password,
                        gender=myform.gender.data, age=myform.age.data)
        register.save()

        return redirect(url_for('webpages.profile_page'))
    return render_template("sign_up.html", form=myform)


@user_blueprint.route('/login')
@user_blueprint.route('/login', methods=['GET', 'POST'])
def log_in():

    myform = LoginForm()

    if myform.validate_on_submit():
        user = User.query.filter_by(email=myform.email.data).first()
        if user:
            if check_password_hash(user.password, myform.password.data):
                return redirect(url_for('webpages.profile_page'))

    return render_template("log_in.html", form=myform)
