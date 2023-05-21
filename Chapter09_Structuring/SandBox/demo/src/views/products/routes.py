from flask import render_template, Blueprint, flash, redirect, url_for

from src.views.products.forms import ProductForm
from src.models import Product
from src.config import Config

from os import path


TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "products")
product_blueprint = Blueprint("products", __name__, template_folder=TEMPLATES_FOLDER)


@product_blueprint.route("/products")
def all_products():
    product_list = Product.query.all()
    return render_template("products.html", prlist=product_list)


@product_blueprint.route("/add_product", methods=["GET", "POST"])
def add_product():
    form = ProductForm()

    if form.validate_on_submit():
        new_product = Product(name=form.name.data, description=form.description.data, price=form.price.data)
        new_product.create()
        return redirect(url_for('products.all_products'))

    return render_template("add_product.html", form=form)


@product_blueprint.route("/edit_product/<int:id>", methods=["GET", "POST"])
def edit_product(id):
    product = Product.query.get(id)
    form = ProductForm(name=product.name, description=product.description, price=product.price)
    if form.validate_on_submit():
        product.name = form.name.data
        product.description = form.description.data
        product.price = form.price.data
        product.save()
        return redirect(url_for('products.all_products'))

    return render_template("add_product.html", form=form)


@product_blueprint.route("/delete_product/<int:id>")
def delete_product(id):
    product = Product.query.get(id)
    product.delete()
    flash("პროდუქტი წაიშალა")
    return redirect(url_for('products.all_products'))


@product_blueprint.route("/products/<int:id>")
def view_product(id):
    chosen_product = Product.query.get(id)
    return render_template("view_product.html", product=chosen_product)