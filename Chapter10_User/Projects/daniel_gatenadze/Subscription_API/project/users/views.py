from flask import Blueprint, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from Chapter10_User.Projects.daniel_gatenadze.Subscription_API.project.users.forms import RegisterForm, LoginForm
from Chapter10_User.Projects.daniel_gatenadze.Subscription_API.project.users.models import User
from Chapter10_User.Projects.daniel_gatenadze.Subscription_API.project.extensions import BaseModel, login_manager
from flask_login import login_user, login_required, logout_user, current_user

auth_blueprint = Blueprint('auth',
                           __name__,
                           template_folder='templates')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@auth_blueprint.route('/register', methods=['GET', 'POST'])
def sign_up():
    myform = RegisterForm()

    if myform.validate_on_submit():
        hashed_password = generate_password_hash(myform.password.data, method='sha256')
        register = User(username=myform.username.data, email=myform.email.data, password=hashed_password,
                        gender=myform.gender.data, age=myform.age.data)
        register.save()

        return redirect(url_for('webpages.profile_page'))
    return render_template("sign_up.html", form=myform)


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def log_in():
    myform = LoginForm()

    if myform.validate_on_submit():
        user = User.query.filter_by(email=myform.email.data).first()
        if user:
            if check_password_hash(user.password, myform.password.data):
                login_user(user)
                flash(f"{user.username} logged in succesfully")
                return redirect(url_for('webpages.profile_page'))
            else:
                flash("Incorrect Credentials")
        else:
            flash("User by that email does not exist")

    return render_template("log_in.html", form=myform)


@auth_blueprint.route('/logout', methods=['GET', 'POST'])
@login_required
def log_out():
    logout_user()
    flash("Succesfully logged out")
    return redirect(url_for('webpages.dashboard'))
