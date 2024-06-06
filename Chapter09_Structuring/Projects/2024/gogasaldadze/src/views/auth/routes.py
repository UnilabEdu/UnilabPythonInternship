from flask import render_template, Blueprint,flash
from src.views.auth.forms import RegisterForm
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
        db.session.add(new_user)
        db.session.commit()  
        flash("წარმატებით დარეგისტრირდით")
    
    return render_template("auth/register.html", form=form)
