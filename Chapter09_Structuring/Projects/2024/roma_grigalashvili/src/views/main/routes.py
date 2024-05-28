from flask import render_template, Blueprint
from os import path

from src.config import Config

TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "main")
main_blueprint = Blueprint("main", __name__, template_folder=TEMPLATES_FOLDER)

top_users_list = [
    {
        "username": "Roma Grigalashvili",
        "gender": "Male",
        "email": "roma.grigalashvili@iliauni.edu.ge",
        "subject": "Math"
    },
    {
        "username": "Saba Dvali",
        "gender": "Male",
        "email": "saba.dvali@iliauni.edu.ge",
        "subject": "History"
    },
    {
        "username": "Tea Godoladze",
        "gender": "Female",
        "email": "tea_godoladze@iliauni.edu.ge",
        "subject": "Math"
    },
    {
        "username": "Roma Grigala",
        "gender": "Male",
        "email": "r.grigalashvili777@gmail.com",
        "subject": "History"
    },
    {
        "username": "Albert Buzaladze",
        "gender": "Male",
        "email": "albert.buzaladze.1@iliauni.edu.ge",
        "subject": "Geography"
    },
]


@main_blueprint.route("/")
def index():
    return render_template("index.html", user_type="admin")

@main_blueprint.route("/highscores")
def highscores():
    return render_template("highscores.html", top_list=top_users_list)