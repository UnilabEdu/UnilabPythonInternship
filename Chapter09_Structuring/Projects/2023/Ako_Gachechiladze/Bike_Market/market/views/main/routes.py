from flask import render_template, Blueprint, request
from market.views.product.forms import FilterProductForm
from market.config import Config
from market.models import Product, User
from os import path
from flask_login import current_user

TEMPALTE_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "main")
main_blueprint = Blueprint("main", __name__, template_folder=TEMPALTE_FOLDER)


@main_blueprint.route("/", methods=['GET', 'POST'])
def home():
    form = FilterProductForm()
    user = User.query.all()
    page = request.args.get('page', 1, type=int)
    products = Product.query.paginate(page=page, per_page=12)

    return render_template("home.html", products=products, form=form, users=user)


