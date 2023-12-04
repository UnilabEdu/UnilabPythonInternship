from flask import render_template, request, Blueprint, redirect, url_for
from flask_login import current_user

from src.models import Petition, User
from src.config import Config
from src.views.petitions.forms import AddPetition

import os

TEMPLATES_FOLDER = os.path.join(Config.BASE_DIRECTORY, "templates", "main")
main = Blueprint("main", __name__, template_folder=TEMPLATES_FOLDER)


@main.route("/", methods=["GET", "POST"])
def home():
    name = request.form.get("search")
    data = Petition.query.all()

    if name:
        data = Petition.query.filter(Petition.title.ilike(f"%{name}%")).all()
        return render_template("index.html", data=data)

    return render_template("index.html", data=data)


@main.route("/contact")
def contact():
    return render_template("errors/working.html")


@main.route("/error", methods=["GET", "POST"])
def error():
    error_code = request.args.get("code")
    return render_template(f"errors/{error_code}.html")
