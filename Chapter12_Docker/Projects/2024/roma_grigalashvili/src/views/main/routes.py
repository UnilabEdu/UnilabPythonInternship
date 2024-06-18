from flask import render_template, Blueprint
from os import path
from src.models import Score

from src.config import Config

TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "main")
main_blueprint = Blueprint("main", __name__, template_folder=TEMPLATES_FOLDER)

@main_blueprint.route("/")
def index():
    return render_template("index.html")

@main_blueprint.route("/highscores")
def highscores():
    top_scores = Score.query.order_by(Score.score.desc()).limit(5).all()
    
    # Format time for each score
    for score in top_scores:
        score.formatted_time = format_time(score.time_taken)
    
    return render_template("highscores.html", top_scores=top_scores)

def format_time(seconds):
    minutes = int(seconds // 60)
    second = int(seconds % 60)
    return f"{minutes} minutes and {second} seconds"
