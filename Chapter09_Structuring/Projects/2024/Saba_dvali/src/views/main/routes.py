from flask import Flask, render_template, redirect, request, Blueprint, url_for
from os import path
from flask_login import login_user, current_user, logout_user
from collections import defaultdict
from uuid import uuid4
import os
from werkzeug.utils import secure_filename

from src.config import Config
# from src.views.main.forms import main
from src.views.auth.forms import RegistrationForm, LoginForm, AddProductForm
from src.models import Users
from src.models import Role
from src.models import Products
from src.models import Images
from src.ext import db


TEMPLATE_FOLDER = path.join(Config.PROJECT_ROOT, "templates", "main")
main_bp = Blueprint("main",__name__, template_folder=TEMPLATE_FOLDER)


# @main_bp.route('/upload_images', methods=['POST', 'GET'])
# def upload_images():
#     product_id = request.form.get('product_id')
#     files = request.files.getlist('images')
#     print(Config.PROJECT_ROOT)
    
#     if files and product_id:
#         product_dir = os.path.join(Config.PROJECT_ROOT, 'images', str(product_id))
#         try:
#             if not os.path.exists(product_dir):
#                 os.makedirs(product_dir)

#             for file in files:
#                 if file.filename != '':
#                     filename = secure_filename(file.filename)
#                     file.save(os.path.join(product_dir, filename))
#                     print(f"Saved file: {filename} in directory: {product_dir}")

#         except Exception as e:
#             print(f"Error creating directory or saving files: {e}")

#     return render_template("imgupload.html")





# @main_bp.route('/drop', methods=['POST',"GET"])
# def upload_images():
#     from sqlalchemy import create_engine, MetaData

#     engine = create_engine("sqlite:///" + path.join(Config.PROJECT_ROOT, "database.db"))

#     metadata = MetaData()
#     metadata.reflect(bind=engine)
#     # Images.delete()
#     your_table = metadata.tables['images']
#     # db.session.table(Images).delete()
#     your_table.drop(engine)

#     return "yes"



# @main_bp.route('/img', methods=['POST',"GET"])
# def upload_images():

#     img = Images(image_name="iphone_11_3.jpg",product_id="6")
    
#     # db.session.query(Products).delete()
#     db.session.add(img)

#     db.session.commit()

#     return "yes"

def add_product():
    form = AddProductForm()
    if form.validate_on_submit():
        product_name =  form.product_name.data
        product_model =  form.product_model.data
        price =  str(form.price.data)
        info =  form.info.data

        addproduct = Products(product_name=product_name,
                            product_model=product_model,
                            price=price,
                            info=info,
                            user_id=current_user.id)
        db.session.add(addproduct)
        db.session.commit()
        product = db.session.query(Products).filter(Products.product_name == product_name,
                                                    Products.product_model == product_model,
                                                    Products.price == price,
                                                    Products.info == info,
                                                    Products.user_id == current_user.id
                                                    ).first()
        if product:
            product_images = request.files.getlist('product_images')
            product_dir = os.path.join(f"{Config.PROJECT_ROOT}/static/images", str(product.id))
            if not os.path.exists(product_dir):
                os.makedirs(product_dir)
                for file in product_images:
                    if file.filename != '':
                        filename = secure_filename(file.filename)
                        file.save(os.path.join(product_dir, filename))
                        img = Images(image_name=filename,product_id=product.id)
                db.session.add(img)
                db.session.commit()

@main_bp.route("/",methods=["GET", "POST"])
def home():
    logform = LoginForm()
    addpoductform = AddProductForm()
    regform = RegistrationForm()

    if addpoductform.validate_on_submit():
        add_product()

    if regform.validate_on_submit():
        print("movida reg")
        user_name = Users.query.filter(Users.name == regform.username_reg.data).first()
        email = Users.query.filter(Users.email == regform.email_reg.data).first()

        if user_name or email:
            print("user name or email is already registred.")
        else:
            add_user=Users(name=regform.username_reg.data,
                           email=regform.email_reg.data,
                           password=regform.password_reg.data,
                           role=2) # static 
            db.session.add(add_user)
            db.session.commit()

    if logform.validate_on_submit():
        print("movida log")

        user = Users.query.filter(Users.name == logform.username_log.data).first()
        if not user:
            print("მითითებული მომხმარებელი ვერ მოიძებნა")
            return redirect("/")
        
        if user.password == logform.password_log.data:
            login_user(user)
            
    products = Products.query.filter().all()
    return render_template("home.html",products=products, regform=regform, logform=logform, addpoductform=addpoductform)


@main_bp.route("/details/<id>")
def details(id):
    product = Products.query.filter(Products.id == id).all()
    for prod in product:
        for img in prod.images:
            print(f"static/images/{img.product_id}/{img.image_name}")
    return render_template("details.html",product=product, regform=RegistrationForm(),logform=LoginForm(),addpoductform=AddProductForm())


@main_bp.route("/profile",methods=["GET", "POST"])
def profile():
    form = AddProductForm()
    if form.validate_on_submit():
        add_product()
    return render_template("profile.html", addpoductform=form)




@main_bp.route("/logout")
def logout():
    logout_user()
    return redirect("/")