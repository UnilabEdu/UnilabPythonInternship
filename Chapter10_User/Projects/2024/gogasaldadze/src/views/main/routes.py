from flask import render_template, Blueprint

main_bp = Blueprint("main",__name__)

@main_bp.route("/")
def index():
    return render_template("main/index.html")

@main_bp.route("/about")
def about():
    return render_template("main/about.html")

@main_bp.route("/materials")
def materials():
    return render_template("main/materials.html")