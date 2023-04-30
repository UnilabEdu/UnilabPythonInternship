from flask import Blueprint, render_template
from src.models.user import User

users_blueprint = Blueprint("users", __name__, template_folder="templates")



@users_blueprint.route("/users")
def users():
    users = User.query.all()

    return render_template("users/users.html", users=users)

