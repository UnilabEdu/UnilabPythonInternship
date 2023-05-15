from flask import Flask, render_template, url_for, flash
from forms import RegisterForm, AboutForm


app = Flask(__name__)

app.config["SECRET_KEY"] = "abgdevztiklm"




@app.route("/", methods=['GET','POST'])
def index():
    form = RegisterForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.birthday.data)
    else:
        flash("error")
        print(form.errors)
    return render_template("index.html", form=form)

@app.route("/about", methods=['GET','POST'])
def about():
    form = AboutForm()
    if form.validate_on_submit():
       print(form.texstarea.data)
       print(form.texstareatwo.data)
    names = ["fitness", "yoga", "crossfit", "pilates", "judo"]
    return render_template("about.html", list_of_names=names, form=form)



if __name__ == "__main__":
    app.run()



