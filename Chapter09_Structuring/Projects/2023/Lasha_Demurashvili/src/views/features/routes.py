from flask import Blueprint, render_template

features_blueprint = Blueprint("features", __name__, template_folder="templates")


@features_blueprint.route("/features")
def features():
    return render_template("features/features.html")
