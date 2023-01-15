from flask import Blueprint, render_template, flash
from os import path, getcwd , sep , pardir
from src.views.registration.forms import Registerform
from werkzeug.utils import secure_filename
from src.models.registration import User
from src.views.registration.name_generator import random_name
from src.extensions import db 

registration_blueprint = Blueprint("reg", __name__, template_folder="templates")

@registration_blueprint.route("/registration", methods=["GET", "POST"])
def registration():
    form = Registerform()
    if form.validate_on_submit():
        

        user_firstname = form.firstname.data
        user_lastname = form.lastname.data
        user_mail = form.email.data
        user_experience = form.writer_experience.data
        user_writer_field = form.writer_field.data
        user_essay_secription = form.essay_description.data


        filename = secure_filename(form.essay_file.data.filename)
        file_type = filename.split(".")[1]

        while True:
            new_filename = random_name() + "." + file_type

            if not User.query.filter_by(uploaded_file = new_filename).first() :


                location = path.realpath(path.join(
                getcwd(), path.dirname(__file__) + sep + pardir+ sep + pardir))
                print(location)
                file_path = path.join(location, "uploaded_files", new_filename)
                form.essay_file.data.save(file_path)
                flash("Succesfully uploaded")


                someone = User(firstname=user_firstname, lastname=user_lastname, email=user_mail,
                                    writer_experience=user_experience, writer_field=user_writer_field, essay_description=user_essay_secription, uploaded_file = new_filename)
                someone.create()
                someone.save()
                break

    else:
        print(form.errors)
    return render_template("registration/registration.html",  register_form=form)

