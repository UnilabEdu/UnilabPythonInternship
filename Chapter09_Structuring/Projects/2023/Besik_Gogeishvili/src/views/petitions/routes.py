from flask import render_template, redirect, url_for, request, Blueprint, flash

from uuid import uuid4
import os

from src.models import Petition, Signer, PetitionSigner
from src.config import Config
from src.views.petitions.forms import AddPetition, SignPetition


TEMPLATES_FOLDER = os.path.join(Config.BASE_DIRECTORY, "templates", "petitions")
petitions = Blueprint("petitions", __name__, template_folder=TEMPLATES_FOLDER)


@petitions.route("/petition/<string:name>")
def petition(name):
    to_display = Petition.query.filter(Petition.url_name == name).scalar()

    return render_template("petition.html", petition=to_display)


@petitions.route("/sign_petition", methods=["GET", "POST"])
def sign_petition():
    form = SignPetition()

    petition_id = request.args.get("petition_id")

    if form.validate_on_submit():

        exists = False

        to_sign = Petition.query.get(petition_id)
        
        for signer in to_sign.signers:
            if signer.personal_id == form.personal_id.data:
                exists = True

        if not exists:
            new_signer = Signer(
                name= form.name.data,
                surname= form.surname.data,
                email= form.email.data,
                personal_id= form.personal_id.data,
                sex= form.sex.data,
                number= form.number.data,
                city= form.city.data,
                date = form.date.data
            )

            new_signer.create()

            petition_signer = PetitionSigner(petition_id=petition_id, signer_id=new_signer.id)
            petition_signer.create()

            to_sign.votes = len(to_sign.signers)
            to_sign.save()

            return redirect(url_for("main.home"))
        else:
            flash("You have already signed this petition!")

    return render_template("sign-form.html", form=form)


@petitions.route("/create_petition", methods=["GET", "POST"])
def create_petition():
    form = AddPetition()

    method = request.args.get("img")


    if form.validate_on_submit():

        name = Config.to_english(form.name.data)

        new_petition = Petition(
            name= form.name.data,
            title= form.title.data,
            address= form.address.data,
            description= form.description.data,
            short_description= form.short_description.data,
            url_name= name,
            img1= form.left_img1_l.data,
            img2= form.left_img2_l.data,
            img3= form.main_img_l.data,
            img4= form.right_img1_l.data,
            img5= form.right_img2_l.data,
            method= "link",
            goal= form.goal.data,
            votes= 0
        )

        if method == "upload":
            new_petition.method = "upload"
            os.makedirs(os.path.join(Config.UPLOAD_PATH, name), exist_ok=True)

            counter = 1
            for key, value in form.data.items():
                if key in Config.UPLOADING_IMAGES:
                    file = value

                    filename, filetype = file.filename.split(".")
                    filename = str(uuid4())
                    fullname = f"{filename}.{filetype}"

                    upload_path = os.path.join(Config.UPLOAD_PATH, name, fullname)
                    file.save(upload_path)

                    setattr(new_petition, f"img{counter}", f"./static/assets/{name}/{fullname}")
                    counter += 1
            

        new_petition.create()

        return redirect(url_for("main.home"))

    return render_template("create-petition.html", form=form, img=method)
