from flask import render_template, Blueprint
from os import path
from uuid import uuid4

from src.views.main.forms import RegisterForm
#from src.config import Config

main_blueprint = Blueprint("main", __name__ template_folder="Templates/main")

@main_blueprint.route("/",methods=["GET", "POST"])
def nutrition():
    form = RegisterForm()

    if form.validate_on_submit():
        new_user=user_input(username=form.username.data, weight_input=form.goal.data)
        db.session.add(new_user)
        db.session.commit()

    else:
        print(form.errors)

    return render_template("/Nutrition1010.html", form=form)