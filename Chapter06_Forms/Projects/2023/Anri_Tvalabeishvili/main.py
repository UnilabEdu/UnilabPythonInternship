from flask import Flask, render_template
from forms import RegisterForm, Auctorisation



app = Flask(__name__)
user_data = []
app.config['SECRET_KEY'] = "Vassalis"


@app.route('/', methods=['GET', 'POST'])
def Sign_Up() :

    Reg = RegisterForm()
    Auto = Auctorisation()

    if Reg.validate_on_submit():
        user_email = Reg.email.data
        user_password = Reg.password.data
        user_username = Reg.username.data

        user = { 
            "user_email": user_email,
            "user_password": user_password,
            "user_username": user_username,
        }

        user_data.append(user)
        return render_template("/User_authorization_registration.html", Reg=Reg, Auto=Auto)


    if Auto.validate_on_submit():
        user_email_autorisation = Auto.email.data
        user_password_autorisation = Auto.password.data
        
        for i in user_data:
            if i["user_email"] == user_email_autorisation and i["user_password"] == user_password_autorisation:
                return render_template("/final.html", user_data=user_data)

                

    return render_template("/User_authorization_registration.html", Reg=Reg, Auto=Auto)




if __name__ == "__main__":
    app.run(debug=True)