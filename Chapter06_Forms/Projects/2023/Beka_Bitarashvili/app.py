from flask import Flask, render_template, url_for, request, flash
from forms import RegisterForm
import os
from uuid import uuid4

app = Flask(__name__)
app.config["SECRET_KEY"] = "12345678"
UPLOAD_PATH = os.path.join(app.root_path, "uploads")


@app.route("/", methods=["GET", "POST"])
def index():
    form = RegisterForm()

    if form.validate_on_submit():
        file = form.profile_pic.data
        filename, filetype = file.filename.split(".")
        filename = str(uuid4())
        directory = os.path.join(UPLOAD_PATH, f"{filename}.{filetype}")
        file.save(directory)

    if form.errors:
        for errors in form.errors.items():
            for error in errors:
                flash("SYSTEM ERROR")

    return render_template("index.html", form=form)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
