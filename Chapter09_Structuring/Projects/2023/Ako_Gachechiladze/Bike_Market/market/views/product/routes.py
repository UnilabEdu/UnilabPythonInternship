from flask import render_template, redirect, url_for, Blueprint, flash
from market.config import Config
from market.models import Product, User
from market.views import ProductForm
from flask_login import login_required, current_user
from os import path

TEMPLATE_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "product")
product_blueprint = Blueprint("products", __name__, template_folder=TEMPLATE_FOLDER)


@product_blueprint.route("/add", methods=['GET', 'POST'])
@login_required
def add_products():
    form = ProductForm()

    if form.validate_on_submit():
        new_product = Product(part=form.part.data,
                              name=form.name.data,
                              description=form.description.data,
                              price=form.price.data,
                              image=form.image.data,
                              owner_id=current_user.id)
        new_product.create()
        return redirect(url_for("products.product_details", id=new_product.id))

    return render_template("add_product.html", form=form)


@product_blueprint.route("/products/<int:id>")
def product_details(id):
    product = Product.query.get(id)
    user = User.query.all()
    return render_template("product_details.html", product=product, users=user)


@product_blueprint.route("/products/edit/<int:id>", methods=['GET', 'POST'])
@login_required
def edit_products(id):
    product = Product.query.get(id)

    form = ProductForm(part=product.part,
                       name=product.name,
                       description=product.description,
                       price=product.price,
                       image=product.image)
    if product.owner_id == current_user.id:
        if form.validate_on_submit():
            product.part = form.part.data
            product.name = form.name.data
            product.description = form.description.data
            product.price = form.price.data
            product.image = form.image.data

            product.save()
            return redirect(url_for("products.product_details", id=product.id))
    else:
        flash("You can't edit product because you are not owner.")

    return render_template("add_product.html", form=form, edit=True)


@product_blueprint.route("/products/delete/<int:id>")
@login_required
def delete_products(id):
    product = Product.query.get(id)
    if product.id == current_user.id:
        product.delete()

    return redirect(url_for("main.home"))
