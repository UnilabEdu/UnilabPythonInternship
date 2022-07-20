from flask import render_template, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from forms import LoginForm, RegisterForm, ProfilePage
from models import SubsPlan, User, db, app



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
        # email = request.form['email']
        # password = request.form['password']

        user = User.query.filter_by(email=myform.email.data).first()
        if user:
            if check_password_hash(user.password, myform.password.data):
                return redirect(url_for('profile_page'))

    return render_template("log_in.html", form=myform)

    #
    # myform = LoginForm()
    # if myform.validate_on_submit():
    #     email = myform.email.data
    #     password = myform.password.data
    #     # fileupload = myform.fileupload.data.save("file.png")
    #     # print(email, password)
    #     session = ['email', 'fileupload', 'password']
    #     email = session[0]
    #
    #     return redirect(url_for('profile_page'))
    #
    # return render_template("log_in.html", form=myform)


@app.route("/register", methods=['GET', 'POST'])
def sign_up():
    myform = RegisterForm()
    if myform.validate_on_submit():
        hashed_password = generate_password_hash(myform.password.data, method='sha256')
        # username = User.username
        # email = request.form['email']
        # password = request.form['password']
        # gender = request.form['gender']
        # age = request.form['age']

        register = User(username=myform.username.data, email=myform.email.data, password=hashed_password,
                        gender=myform.gender.data, age=myform.age.data)
        db.session.add(register)
        db.session.commit()

        return redirect(url_for('profile_page'))
    return render_template("sign_up.html", form=myform)

    # myform = RegisterForm()
    # if myform.validate_on_submit():
    #     username = myform.username.data
    #     email = myform.email.data
    #     password = myform.password.data
    #     confirmpassword = myform.password.data
    #     gender = myform.gender.data
    #     age = myform.age.data
    #
    #     item = User()
    #     item.create(username=username, email=email, password=password, gender=gender, age=age, commit=True)
    #
    #     # fileupload = myform.fileupload.data.save(f'user_avatars/file.png')
    #     # print(username, email, password, confirmpassword, gender, age)
    #     flask.session = ['username', 'email', 'gender', 'age', 'fileupload']
    #     # username, email, gender, age, fileupload = session[0], session[1], session[2], session[3], session[4]
    #     username = flask.session[0]
    #     email = flask.session[1]
    #     gender = flask.session[2]
    #     age = flask.session[3]
    #     fileupload = flask.session[4]
    #     return redirect(url_for('profile_page'))
    #
    # return render_template("sign_up.html", form=myform)


@app.route("/profile_page")
def profile_page():
    myform = ProfilePage()
    return render_template("profile_page.html", form=myform)


if __name__ == "__main__":
    app.run(debug=True)
