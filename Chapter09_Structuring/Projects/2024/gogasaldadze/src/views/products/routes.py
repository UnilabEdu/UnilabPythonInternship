from flask import render_template,Blueprint,redirect, flash
from src.ext import db
from src.config import Config
from src.views.products.forms import ProductForm
products_bp = Blueprint("products",__name__)
from uuid import uuid4
from os import path
from src.models.products import Products

@products_bp.route("/add_product",methods = ["GET","POST"])
def add_products():
    form = ProductForm()
    if form.validate_on_submit():
        product = Products(name=form.name.data, price=form.price.data, img =None)
        if form.img.data != None:
         img = form.img.data
         filename, extension = path.splitext(img.filename)
         filename = str(uuid4())
         directory = path.join(Config.PROJECT_ROOT, "static", "uploads", f"{filename}{extension}")
         img.save(directory)
         product.img = f"{filename}{extension}"
        db.session.add(product)
        db.session.commit()
        flash("წარმატებით დარეგისტრირდით")
    return render_template("products/add_product.html", form=form)

@products_bp.route("/edit_product/<int:product_id>",methods =["GET","POST"])
def edit_product(product_id):
    product = Products.query.get(product_id)


    if not product:
        flash("პროდუქტი არ მოიძებნა")

    form = ProductForm(obj = product)
    if form.validate_on_submit():
        product.name = form.name.data
        product.price = form.price.data

        if not type (form.img.data)==str:
             
             img = form.img.data
             filename, extension = path.splitext(img.filename)
             filename = str(uuid4())
             directory = path.join(Config.PROJECT_ROOT, "static", "uploads", f"{filename}{extension}")
             img.save(directory)
             product.img = f"{filename}{extension}"
            
    db.session.commit()
    flash("წარმატებით დარეგისტრირდით")     

    return render_template("products/add_product.html",form=form)



@products_bp.route("/products")
def products():
    prod = Products.query.all()
    return render_template("products.html", prod=prod)

@products_bp.route("/products/<int:id>")
def view_product(id):
    product = Products.query.get_or_404(id)  
    return render_template("products/viewproduct.html", product=product)  
