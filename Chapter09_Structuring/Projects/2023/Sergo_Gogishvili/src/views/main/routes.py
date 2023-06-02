from flask import render_template, Blueprint, flash, url_for
from os import path
from uuid import uuid4

from src.views.main.forms import RegisterForm
from src.config import Config

TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "main")
main_blueprint = Blueprint("main", __name__, template_folder=TEMPLATES_FOLDER)

@main_blueprint.route("/", methods=['GET','POST'])
def index():
    form = RegisterForm()
    if form.validate_on_submit():
        user_username = form.username.data
        user_password = form.password.data
        users = User(username=user_username, password=user_password)
    else:
        flash("error")
        print(form.errors)
    return render_template("index.html", form=form)

@main_blueprint.route("/about", methods=['GET','POST'])
def about():
    form = AboutForm()
    if form.validate_on_submit():
       print(form.texstarea.data)
       print(form.texstareatwo.data)
    names = ["fitness", "yoga", "crossfit", "pilates", "judo"]
    return render_template("about.html", list_of_names=names, form=form)