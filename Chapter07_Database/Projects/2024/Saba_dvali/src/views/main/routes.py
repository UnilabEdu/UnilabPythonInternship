from flask import Flask, render_template, redirect, request, Blueprint, url_for
from os import path

from data import products
from src.config import Config
# from src.views.main.forms import main
from src.views.auth.forms import RegistrationForm, LoginForm


TEMPLATE_FOLDER = path.join(Config.PROJECT_ROOT, "templates", "main")
main_bp = Blueprint("main",__name__, template_folder=TEMPLATE_FOLDER)


validation = False


@main_bp.route("/",methods=["GET", "POST"])
def home():
    global validation
    regform = RegistrationForm()
    logform = LoginForm()
    if regform.validate_on_submit():
        print("reg")
        validation = True
    if logform.validate_on_submit():
        print("log")
        validation = True
        
    return render_template("home.html",products=products.products, regform=regform, logform=logform, validation=validation)


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
    global validation

    if validation:  
        return render_template("profile.html", validation=validation)
    else:
        return "hello"
