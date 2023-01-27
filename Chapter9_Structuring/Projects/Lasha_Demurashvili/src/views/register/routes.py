from src.views.register.forms import RegisterForm
from flask import Blueprint, render_template, flash
from src.models.user import User
from src.extensions import db

register_blueprint = Blueprint("register", __name__, template_folder="templates")


@register_blueprint.route("/register", methods=["GET", "POST"])
def register():
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

        return render_template("register/register.html", register_form=form)


    return render_template("register/register.html", register_form=form)