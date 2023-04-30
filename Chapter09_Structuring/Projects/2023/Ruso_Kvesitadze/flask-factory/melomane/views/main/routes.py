from flask import Blueprint, render_template

main_blueprint = Blueprint("main", __name__, template_folder="templates")

@main_blueprint.route("/")
def melomane():
    return render_template("main/Melomane.html")

