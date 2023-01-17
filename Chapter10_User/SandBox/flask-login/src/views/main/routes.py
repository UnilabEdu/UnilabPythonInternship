from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required
from src.utils import admin_required

main_blueprint = Blueprint("main", __name__, template_folder="templates")


@main_blueprint.route("/")
def index():
    return render_template("main/index.html")