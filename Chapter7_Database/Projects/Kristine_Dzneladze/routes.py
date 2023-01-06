from flask import render_template, flash
from werkzeug.utils import secure_filename
from forms import Registerform
from os import path, getcwd

from app import app,db
from Models import RegisterForm



@app.before_first_request
def create_db():
    db.create_all()
    if len(RegisterForm.query.all()) == 0:
        user = [ 
        ("Kristine", "Dzneladze","kristinedzneladze@mail.com", "Begginer Writer", "Personal essay", "This is description1"),
        ("Anri", "Dzneladze","Anridzneladze@mail.com", "Experienced Writer", "Personal essay", "This is description2")
        ]
        for person in user :
            someone = RegisterForm(firstname = person[0], lastname = person[1], email = person[2], writer_experience = person[3], writer_field = person[4],essay_description  = person[5])
            db.session.add(someone)
        db.session.commit()

    




@app.route("/")
def home():
    return render_template("home.html")


@app.route("/forms", methods=["GET", "POST"])
def forms():
    form = Registerform()
    if form.validate_on_submit():


        user_firstname = form.firstname.data
        user_lastname = form.lastname.data
        user_mail =   form.email.data
        user_experience = form.writer_experience.data
        user_writer_field = form.writer_field.data
        user_essay_secription =  form.essay_description.data

        someone = RegisterForm(firstname = user_firstname, lastname = user_lastname, email = user_mail, writer_experience = user_experience, writer_field = user_writer_field, essay_description  = user_essay_secription)
        db.session.add(someone)
        db.session.commit()

        filename = secure_filename(form.essay_file.data.filename)

        location = path.realpath(path.join(
            getcwd(), path.dirname(__file__)))
        file_path = path.join(location, "uploaded_files", filename)
        form.essay_file.data.save(file_path)
        flash("Succesfully uploaded")
    else:
        print(form.errors)
    return render_template("forms.html",  register_form=form)


@app.route("/youruploadedinfo")
def yourinfo():
    all_data  = (list(RegisterForm.query.all()))
    print(all_data[0].firstname)


        
    return render_template("yourinfo.html", info=all_data)
