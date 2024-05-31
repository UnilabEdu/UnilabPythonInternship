from flask import render_template, Blueprint, flash, redirect, url_for
from flask_login import login_required, current_user
from os import path

from src.views.products.forms import ProductForm
from src.models import Product, UserProduct
from src.config import Config

TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "products")
product_blueprint = Blueprint("products", __name__, template_folder=TEMPLATES_FOLDER)

@product_blueprint.route("/products")
def all_products():
    product_list = Product.query.all()
    return render_template("products.html", prlist=product_list)


@product_blueprint.route("/add_product", methods=["GET", "POST"])
@login_required
def add_product():
    form = ProductForm()

    if not current_user.is_admin():
        return redirect("/")

    if form.validate_on_submit():
        new_product = Product(name=form.name.data, description=form.description.data, price=form.price.data)
        new_product.create()

        user_product = UserProduct(user_id=current_user.id, product_id=new_product.id)
        user_product.create()

        return redirect("/products")
    return render_template("add_product.html", form=form)


@product_blueprint.route("/edit_product/<int:id>", methods=["GET", "POST"])
@login_required
def edit_product(id):
    product = Product.query.get(id)
    form = ProductForm(name=product.name, description=product.description, price=product.price)
    if form.validate_on_submit():
        product.name = form.name.data
        product.description = form.description.data
        product.price = form.price.data
        product.save()
        return redirect("/products")

    return render_template("add_product.html", form=form)


@product_blueprint.route("/delete_product/<int:id>")
def delete_product(id):
    product = Product.query.get(id)
    product.delete()
    flash("პროდუქტი წაიშალა")
    return redirect("/products")


@product_blueprint.route("/product/<int:id>")
def view_product(id):
    chosen_product = Product.query.get(id)

    if current_user.id != chosen_product.user.id:
        flash("ეს პროდუქტ თქვენი არ არის")
        return redirect("/")

    return render_template("view_product.html", product=chosen_product)