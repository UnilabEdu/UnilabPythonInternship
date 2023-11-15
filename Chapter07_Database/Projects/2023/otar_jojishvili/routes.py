from app import app
from forms import LogUser, AddUser
from models import Users
from flask import Flask, render_template, request, redirect
from db import db


registered_user = ''
logged_user_name = None

@app.route('/', methods=["POST", "GET"])
def sign():
    form = LogUser()
    global logged_user_name
    if request.method == 'POST':
        entered_email = form.loguser_email.data
        all_mail = Users.query.with_entities(Users.email).all()
        all_mail_list = []
        for mail in all_mail:
            index_of_mail = all_mail.index(mail)
            mail_from_tuple = all_mail[index_of_mail]
            formatted_mail = mail_from_tuple[0]
            all_mail_list.append(formatted_mail)
        if form.validate_on_submit():
           if entered_email in all_mail_list:
               logged_user = Users.query.filter_by(email=entered_email).first()
               if form.loguser_password.data == logged_user.password:
                   print("Logged Succesfully!")
                   logged_user_name =logged_user.name
                   return redirect("home")
               else:
                   print("Wrong Password")
           else:
                print("Wrong mail!")
    return render_template("sign.html", form=form)


@app.route("/register", methods=["POST", "GET"])
def register():
    form = AddUser()
    global logged_user_name
    if request.method == "POST":
        if form.validate_on_submit():
            new_user = Users(
                name = form.user_name.data,
                surname = form.user_surname.data,
                email = form.user_email.data,
                password = form.user_password.data
            )
            db.session.add(new_user)
            db.session.commit()
            print("add   ed succesfully")
            return redirect('home')
    return render_template("register.html", form=form)


@app.route("/home")
def home():
    global logged_user_name
    return render_template("home.html",logged_user_name =logged_user_name)


@app.route("/about_us")
def about():
    return render_template("about_us.html")