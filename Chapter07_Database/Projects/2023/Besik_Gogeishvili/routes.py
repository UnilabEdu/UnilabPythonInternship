from flask import render_template, redirect, url_for, request
from forms import AddPetition, Register, Login
from models import Petition
from db import db
from app import app, to_english, UPLOAD_PATH, data, UPLOADING_IMAGES
from uuid import uuid4
import os


@app.route("/", methods=["GET", "POST"])
def home():
    name = request.form.get("search")
    data = Petition.query.all()

    if name:
        data = Petition.query.filter(Petition.title.ilike(f"%{name}%")).all()
        return render_template("index.html", data=data)

    return render_template("index.html", data=data)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = Login()

    if form.validate_on_submit():
        print("passed")
        return redirect(url_for("home"))

    return render_template("login.html", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = Register()

    if form.validate_on_submit():
        print("passed")
        return redirect(url_for("home"))

    return render_template("register.html", form=form)


@app.route("/petition/<string:name>")
def petition(name):
    to_display = Petition.query.filter(Petition.url_name == name).scalar()
    
    print(to_display)

    return render_template("petition.html", petition=to_display)


@app.route("/sign_petition")
def sign_petition():
    return render_template("sign-form.html")


@app.route("/create_petition", methods=["GET", "POST"])
def create_petition():
    form = AddPetition()

    method = request.args.get("img")


    if form.validate_on_submit():

        name = to_english(form.name.data)

        new_petition = Petition(
            name= form.name.data,
            title= form.title.data,
            adress= form.address.data,
            description= form.description.data,
            short_description= form.short_description.data,
            url_name= name,
            img1= form.left_img1_l.data,
            img2= form.left_img2_l.data,
            img3= form.main_img_l.data,
            img4= form.right_img1_l.data,
            img5= form.right_img2_l.data,
            method= "link"
        )

        if method == "upload":
            new_petition.method = "upload"
            os.makedirs(os.path.join(UPLOAD_PATH, name), exist_ok=True)

            counter = 1
            for key, value in form.data.items():
                if key in UPLOADING_IMAGES:
                    file = value

                    filename, filetype = file.filename.split(".")
                    filename = str(uuid4())
                    fullname = f"{filename}.{filetype}"

                    upload_path = os.path.join(UPLOAD_PATH, name, fullname)
                    file.save(upload_path)

                    setattr(new_petition, f"img{counter}", f"./static/assets/{name}/{fullname}")
                    counter += 1
            

        new_petition.create()

        return redirect(url_for("home"))

    return render_template("create-petition.html", form=form, img=method)


@app.route("/contact")
def contact():
    return render_template("working.html")
