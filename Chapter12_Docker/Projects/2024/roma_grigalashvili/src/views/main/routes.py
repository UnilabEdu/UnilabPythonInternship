from flask import render_template, Blueprint
from os import path
from src.models import Score

from src.config import Config

TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "main")
main_blueprint = Blueprint("main", __name__, template_folder=TEMPLATES_FOLDER)

# top_users_list = [
#     {
#         "username": "Roma Grigalashvili",
#         "email": "roma.grigalashvili@iliauni.edu.ge",
#         "quiz": "Quiz in Geography",
#         "score": 8

#     },
#     {
#         "username": "Saba Dvali",
#         "email": "saba.dvali@iliauni.edu.ge",
#         "quiz": "Quiz in Geography",
#         "score": 8
#     },
#     {
#         "username": "Tea Godoladze",
#         "email": "tea_godoladze@iliauni.edu.ge",
#         "quiz": "Quiz in Programmig",
#         "score": 8
#     },
#     {
#         "username": "Roma Grigala",
#         "email": "r.grigalashvili777@gmail.com",
#         "quiz": "Quiz in Programmig",
#         "score": 9
#     },
# ]


@main_blueprint.route("/")
def index():
    return render_template("index.html")

@main_blueprint.route("/highscores")
def highscores():
    top_scores = Score.query.order_by(Score.score.desc()).limit(5).all()
    
    return render_template("highscores.html", top_scores=top_scores)