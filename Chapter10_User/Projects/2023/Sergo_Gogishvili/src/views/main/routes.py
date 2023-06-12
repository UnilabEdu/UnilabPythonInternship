from flask import render_template, Blueprint, flash, url_for
from os import path
from uuid import uuid4
from flask_login import current_user
from src.models import User
from src.views.main.forms import RegisterForm, AboutForm
from src.config import Config

TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "main")
main_blueprint = Blueprint("main", __name__, template_folder=TEMPLATES_FOLDER)


@main_blueprint.route("/", methods=["GET", "POST"])
def index():
    form = RegisterForm()

    if form.validate_on_submit():
        file = form.profile_picture.data
        filename, filetype = file.filename.split(".")
        filename = str(uuid4())
        directory = path.join(Config.UPLOAD_PATH, f"{filename}.{filetype}")
        file.save(directory)

    if form.errors:
        for errors in form.errors.values():
            for error in errors:
                flash(error)

    return render_template("index.html", user_type="admin", form=form)


@main_blueprint.route("/about", methods=['GET','POST'])
def about():
    form = AboutForm()
    if form.validate_on_submit():
       print(form.texstarea.data)
       print(form.texstareatwo.data)
    names = ["fitness", "yoga", "crossfit", "pilates", "judo"]
    return render_template("about.html", list_of_names=names, form=form)