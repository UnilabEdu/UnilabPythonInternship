from flask import render_template, Blueprint
from market.config import Config
from market.models import Product, User
from flask_login import login_required
from os import path

TEMPLATE_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "profile")
profile_blueprint = Blueprint("profiles", __name__, template_folder=TEMPLATE_FOLDER)


@profile_blueprint.route("/profile/<username>")
def profile(username):
    user = User.query.filter_by(username=username).first()
    user_products = Product.query.filter_by(owner_id=user.id)
    return render_template("profile.html", products=user_products, user=user)
