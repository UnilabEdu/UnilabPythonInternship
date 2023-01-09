from flask import Flask, render_template, request, flash , session
from werkzeug.utils import secure_filename
from forms import Registerform
from os import getcwd, path 
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysectretkey"

info_list=[]

@app.route("/")
def home():
    return render_template("home.html" , info = info_list)

@app.route("/forms", methods = ["GET", "POST"])
def forms():
    form = Registerform()
    if form.validate_on_submit():
            my_info = {
                "firstname": form.firstname.data,
                "lastname":form.lastname.data,
                "email": form.email.data,
                "essay_description": form.essay_description.data
            }
            info_list.append(my_info)

            filename = secure_filename(form.essay_file.data.filename)

            location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
            file_path = path.join(location,"uploaded_files", filename)
            form.essay_file.data.save(file_path)
            flash("Succesfully uploaded")
    else:
            print(form.errors)
    return render_template("forms.html",  register_form = form)


@app.route("/youruploadedinfo")  
def yourinfo():
    return render_template("yourinfo.html", info=info_list)

if __name__ == "__main__":
    app.run(debug=True)