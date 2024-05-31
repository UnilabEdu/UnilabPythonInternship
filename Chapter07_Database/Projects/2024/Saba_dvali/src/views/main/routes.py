from flask import Flask, render_template, redirect, request, Blueprint, url_for
from os import path
from flask_login import login_user, current_user
from collections import defaultdict

from data import products as abc
from src.config import Config
# from src.views.main.forms import main
from src.views.auth.forms import RegistrationForm, LoginForm
from src.models import Users
from src.models import Role
from src.models import Products
from src.models import Images
from src.ext import db


TEMPLATE_FOLDER = path.join(Config.PROJECT_ROOT, "templates", "main")
main_bp = Blueprint("main",__name__, template_folder=TEMPLATE_FOLDER)


# validation = False
# @main_bp.route('/upload_images', methods=['POST',"GET"])
# def upload_images():
#     product_id = request.form.get('product_id')
#     files = request.files.getlist('images')

#     for file in files:
#         image_data = file.read()
#         new_image = Images(image=image_data, product_id=product_id)
#         db.session.add(new_image)
    
#     db.session.commit()
#     # Images.query.delete()
#     # db.session.commit()

#     return render_template("imgupload.html")



@main_bp.route("/",methods=["GET", "POST"])
def home():
    # global validation
    regform = RegistrationForm()
    logform = LoginForm()
    if regform.validate_on_submit():
        print("reg")

        # validation = True
    if logform.validate_on_submit():
        user = Users.query.filter(Users.name == logform.username_log.data).first()
        if not user:
            print("ეს მომხმარებელი ვერ მოიძებნა")
            return redirect("/")
        
        if user.password == logform.password_log.data:
            login_user(user)
            return redirect("/profile")
    return render_template("home.html",products=abc.products, regform=regform, logform=logform)


@main_bp.route("/details/<id>")
def details(id):

    for modelkey, modelname in products.products.items():
        for models, product in modelname.items():
            if product["id"] == id:
                prod = product
                return render_template("details.html",prod=prod)
    return redirect(url_for('/'))



@main_bp.route("/profile")
def profile():

    products = Products.query.filter(Products.user_id == current_user.id).all()
    # images = Images.query.filter(Images.product_id == current_user.id).all()
    product_ids = [product.id for product in products]
    images = Images.query.filter(Images.product_id.in_(product_ids)).all()

    images_by_product = defaultdict(list)
    for image in images:
        images_by_product[image.product_id].append(image)

    product = []

    for i in images_by_product:
        print(i)



    return render_template("profile.html")
