from os import path
from flask import Blueprint, render_template

from src.config import Config


TEMPLATE_FOLDER = path.join(Config.TEPMLATE_FOLDER, "main")
main = Blueprint("main", __name__, template_folder=TEMPLATE_FOLDER)


@main.get("/")
@main.get("/home")
def main_get():
    return render_template("main.html", title="Home Page")
