from flask import render_template, Blueprint
from os import path

from src.config import Config

TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "main")
main_blueprint = Blueprint("main", __name__, template_folder=TEMPLATES_FOLDER)

top_users_list = [
    {
        "username": "Roma Grigalashvili",
        "email": "roma.grigalashvili@iliauni.edu.ge",
        "subject": "Math",
        "score": 40

    },
    {
        "username": "Saba Dvali",
        "email": "saba.dvali@iliauni.edu.ge",
        "subject": "History",
        "score": 38
    },
    {
        "username": "Tea Godoladze",
        "email": "tea_godoladze@iliauni.edu.ge",
        "subject": "Math",
        "score": 37
    },
    {
        "username": "Roma Grigala",
        "email": "r.grigalashvili777@gmail.com",
        "subject": "History",
        "score": 39
    },
    {
        "username": "Albert Buzaladze",
        "email": "albert.buzaladze.1@iliauni.edu.ge",
        "subject": "Geography",
        "score": 37
    },
]


@main_blueprint.route("/")
def index():
    return render_template("index.html")

@main_blueprint.route("/highscores")
def highscores():
    return render_template("highscores.html", top_list=top_users_list)

@main_blueprint.route("/game")
def game():
    return render_template("game.html", top_list=top_users_list)