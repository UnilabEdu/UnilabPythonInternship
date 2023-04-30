from flask import Blueprint, render_template, request, redirect, url_for
from app.views.Login_Signup.forms import SignupForm, LoginForm,Logout
from app.models.user import User
from flask_login import login_user, logout_user, login_required

reg_auto_blueprint = Blueprint("reg_auto", __name__, template_folder="templates")






@reg_auto_blueprint.route("/registration authorisation", methods=["GET", "POST"])
def registration_authorisation():

    Signup_form = SignupForm()
    Login_form = LoginForm()



    if Signup_form.validate_on_submit():

        existing_user = bool(User.query.filter_by(mail = Signup_form.email.data).first())

        if not existing_user:
            
            name = Signup_form.name_and_surname.data
            number = Signup_form.mobile_number.data
            mail = Signup_form.email.data
            password = Signup_form.password.data
            adress = Signup_form.address.data
            Type = "User"


            user = User(name=name, number=number, mail=mail,password=password, adress=adress, Type=Type)

            user.create()
            user.save()


            print("მომხმარებელი დამატებულია")       # ფლეში მინდა ამაზე
        else:
            print("ასეთი მომხმარებელი არსებობს")  # ფლეში მინდა ამაზე

    


    if Login_form.validate_on_submit():

        user = User.query.filter_by(mail = Login_form.email.data).first()

        if user and user.check_password(Login_form.password.data):
            login_user(user)

            return render_template('main/Home.html')




    return render_template("Login_Signup/Login_Signup.html", Signup_form = Signup_form , Login_form =Login_form )





@reg_auto_blueprint.route("/user profile", methods=["GET", "POST"])
@login_required
def profile():

    form = Logout()

    if request.method == 'POST':
        logout_user()
        return render_template("main/Home.html")

    return render_template("Login_Signup/profile.html", form = form)