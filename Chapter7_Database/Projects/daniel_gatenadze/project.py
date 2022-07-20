from flask import Flask, render_template, flash, redirect, url_for, session
from forms import LoginForm, RegisterForm, Profile_Page

app = Flask(__name__)
app.config['SECRET_KEY'] = "CinToa$T"


@app.route("/")
def dashboard():
    return render_template("main.html")


@app.route("/products")
def products():
    return render_template("products.html")


@app.route("/flipacoin")
def flipacoin():
    return render_template("flipacoin.html")


@app.route("/login", methods=['GET', 'POST'])
def log_in():
    myform = LoginForm()
    if myform.validate_on_submit():
        email = myform.email.data
        password = myform.password.data
        # fileupload = myform.fileupload.data.save("file.png")
        # print(email, password)
        session = ['email', 'fileupload', 'password']
        email = session[0]

        return redirect(url_for('profile_page'))

    return render_template("log_in.html", form=myform)


@app.route("/register", methods=['GET', 'POST'])
def sign_up():
    myform = RegisterForm()
    if myform.validate_on_submit():
        username = myform.username.data
        email = myform.email.data
        password = myform.password.data
        confirmpassword = myform.password.data
        gender = myform.gender.data
        age = myform.age.data
        # fileupload = myform.fileupload.data.save(f'user_avatars/file.png')
        # print(username, email, password, confirmpassword, gender, age)
        # session = ['username', 'email', 'gender', 'age', 'fileupload']
        # username, email, gender, age, fileupload = session[0], session[1], session[2], session[3], session[4]
        return redirect(url_for('profile_page'))

    return render_template("sign_up.html", form=myform)


@app.route("/profile_page")
def profile_page():
    myform = Profile_Page()
    return render_template("profile_page.html", form=myform)


if __name__ == "__main__":
    app.run(debug=True)
