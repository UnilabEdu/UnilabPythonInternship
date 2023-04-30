from flask import Blueprint, render_template
from src.models.product import Product

pricing_blueprint = Blueprint("pricing", __name__, template_folder="templates")


@pricing_blueprint.route("/pricing")
def pricing():
    products = Product.query.all()

    return render_template("pricing/pricing.html", products=products)

