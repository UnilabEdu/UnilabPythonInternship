from flask import render_template, redirect, url_for, request, Blueprint
from flask_login import current_user, login_required

import os

from src.models import Petition, User
from src.config import Config
from src.views.user.forms import EditPetition, EditUser

TEMPLATES_FOLDER = os.path.join(Config.BASE_DIRECTORY, "templates", "user")
user = Blueprint("user", __name__, template_folder=TEMPLATES_FOLDER)


@user.route("/user/<string:username>", methods=["GET", "POST"])
def user_profile(username):
    signed = []
    user_prof = User.query.filter(User.username == username).first()

    if user_prof is None:
        return redirect(url_for("main.error", code="404"))

    data = Petition.query.filter(Petition.user_id == user_prof.id).all()
    petitions = Petition.query.all()

    for petition in petitions:
        for each in petition.signers:
            if each.email == user_prof.email:
                signed.append(petition)

    if current_user.is_authenticated and current_user.id == user_prof.id:

        form = EditUser(
            name=user_prof.name,
            surname=user_prof.surname,
        )

        if form.validate_on_submit and request.method == "POST":
            user_prof.name = form.name.data
            user_prof.surname = form.surname.data
            user_prof.password = form.password.data

            user_prof.save()

        return render_template("user.html", user=user_prof, form=form, data=data, signed=signed,
                               count=[len(data), len(signed)])

    return render_template("guest_user.html", user=user_prof, data=data, signed=signed,
                           count=[len(data), len(signed)])


@user.route("/delete/<int:id>")
def delete(id):
    petition = Petition.query.get(id)

    petition.remove()

    return redirect(url_for("user.user_profile", username=current_user.username))


@user.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    petition = Petition.query.get(id)
    form = EditPetition(
        name=petition.name,
        title=petition.title,
        address=petition.address,
        description=petition.description,
        short_description=petition.short_description,
    )

    petition.name = form.name.data
    petition.title = form.title.data
    petition.address = form.address.data
    petition.description = form.description.data
    petition.short_description = form.short_description.data

    return render_template("edit_petition.html", user=user, form=form)
