from flask import Blueprint, render_template

index_blueprint = Blueprint('index', __name__, static_folder='static', template_folder='templates')


@index_blueprint.route("/", methods=["GET","POST"])
def index():
    return render_template("index.html")