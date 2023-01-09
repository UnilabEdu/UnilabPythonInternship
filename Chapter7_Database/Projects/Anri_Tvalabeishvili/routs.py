from flask import render_template
from main import app, db

from forms import RegisterForm, Auctorisation
from model import users


@app.before_first_request
def create_db():
    db.create_all()

    if len(users.query.all()) == 0:
        user = [
                ("anri tvalabeishvili", "anri.tvalabeishvili@gmail.com", "Vessalius154"),
                ("anri tvalabeishvili2", "anri.tvalabeishvili2@gmail.com", "Vessalius155"),
                ("anri tvalabeishvili3", "anri.tvalabeishvili3@gmail.com", "Vessalius156"), ]

        for person in user:
            person = users(username=person[0], email=person[1], password=person[2])
            db.session.add(person)    
        db.session.commit()





@app.route('/', methods=['GET', 'POST'])
def Sign_Up() :

    Reg = RegisterForm()
    Auto = Auctorisation()

    if Reg.validate_on_submit():
        user_email = Reg.email.data
        user_password = Reg.password.data
        user_username = Reg.username.data

        user = users(username = user_username, email = user_email, password= user_password )
        db.session.add(user)
        db.session.commit()

        return render_template("/User_authorization_registration.html", Reg=Reg, Auto=Auto)


    if Auto.validate_on_submit():
        user_email_autorisation = Auto.email.data
        user_password_autorisation = Auto.password.data

       
        user_exist = bool(db.session.query(users.email).filter(users.email==user_email_autorisation).first())
        
        if user_exist:
            real_password = db.session.query(users.password).filter(users.email == user_email_autorisation).first()

            if real_password[0] == user_password_autorisation:

                return render_template ("final.html")

            print(real_password)
        


                

    return render_template("/User_authorization_registration.html", Reg=Reg, Auto=Auto)

