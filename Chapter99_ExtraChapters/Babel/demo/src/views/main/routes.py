from flask import render_template, Blueprint, session, redirect, url_for
from os import path

from src.config import Config

TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "main")
main_blueprint = Blueprint("main", __name__, template_folder=TEMPLATES_FOLDER)


@main_blueprint.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@main_blueprint.route("/about")
def about():
    return render_template("about.html")


@main_blueprint.route("/change_language")
def change_language():
    if session['locale'] == 'ka':
        session['locale'] = 'en'
    else:
        session['locale'] = 'ka'

    return redirect(url_for('main.index'))
