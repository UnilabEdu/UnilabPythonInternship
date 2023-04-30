from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required
from src.views.products.forms import ProductForm
from src.models.product import Product, ProductCategory

products_blueprint = Blueprint("product", __name__, template_folder="templates")


@products_blueprint.route("/products")
def products():
    products = Product.query.all()
    return render_template("products/products.html", products=products)


@products_blueprint.route("/add_product", methods=['GET', 'POST'])
@login_required
def add_product():
    product_form = ProductForm()
    if product_form.validate_on_submit():
        category = ProductCategory.query.filter_by(name=product_form.product_category.data).first()
        product = Product(name=product_form.product_name.data, price=product_form.price.data, category_id=category.id)
        product.create()
        return redirect(url_for('product.products'))
    return render_template("products/add_product.html", form=product_form)


@products_blueprint.route("/edit_product/<int:product_id>", methods=['GET', 'POST'])
def edit_product(product_id):
    product = Product.query.get(product_id)
    product_form = ProductForm()

    if product_form.validate_on_submit():
        product.name = product_form.product_name.data
        product.price = product_form.price.data

        category = ProductCategory.query.filter_by(name=product_form.product_category.data).first()
        product.category_id = category.id
        product.save()
        return redirect(url_for('product.products'))
    return render_template("products/edit_product.html", product=product, form=product_form)


@products_blueprint.route("/delete_product/<int:product_id>")
def delete_product(product_id):
    product = Product.query.get(product_id)
    product.delete()
    return redirect(url_for('product.products'))