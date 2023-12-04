from flask import render_template, request, Blueprint, session

from src.models import Petition
from src.config import Config

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
    return render_template("layouts/working.html")
