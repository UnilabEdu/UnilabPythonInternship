from flask import render_template, Blueprint,flash,redirect, request
from flask_login import login_user, logout_user
from src.views.auth.forms import RegisterForm,LoginForm
from src.models.Users import Users
from src.ext import db


auth_bp = Blueprint("auth",__name__)


@auth_bp.route("/register", methods=["POST", "GET"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = Users(username=form.username.data, 
                         password=form.password.data,           
                         age=form.age.data,
                         gender=form.gender.data,
                         nationality=form.nationality.data)
        new_user.create()
        flash("წარმატებით დარეგისტრირდით")
    
    return render_template("auth/register.html", form=form)


@auth_bp.route("/login",methods = ["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter(Users.username ==form.username.data).first()
        if not user:
            flash('მომხმარებელი ვერ მოიძებნა')
            return redirect("/login")
        if user.password == form.password.data:

            login_user(user)
        next = request.args.get("next")
        if next:
            return redirect(next)
        else:
            return redirect("/")
    return render_template("auth/login.html",form= form)

@auth_bp.route("/logout")
def logout():
    logout_user()
    flash('თქვენ დალოგაუთდით')
    return  redirect("/")