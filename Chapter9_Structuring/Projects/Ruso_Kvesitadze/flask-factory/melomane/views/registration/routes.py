from flask import Blueprint, render_template, flash
from melomane.views.registration.forms import RegisterForm
from melomane.models.users import User
from melomane.extensions import db

registration_blueprint = Blueprint("registration", __name__, template_folder="templates")

@registration_blueprint.route("/forms", methods =["GET", "POST"])
def registration():
    form = RegisterForm()
    if form.validate_on_submit():
        user_username = form.username.data
        user_email = form.email.data
        user_password = form.password.data
        person = User(username=user_username, email=user_email, password=user_password)
        db.session.add(person)
        db.session.commit()


        flash("succesfully registered")
    else:
        print(form.errors)

        return render_template("registration/registration.html", register_form=form)


    return render_template("registration/registration.html", register_form=form)
