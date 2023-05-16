from flask import Flask, render_template, url_for, flash
from forms import RegisterForm
import os
from uuid import uuid4

app = Flask(__name__)
app.config["SECRET_KEY"] = "kljadskl10248120318znx"
UPLOAD_PATH = os.path.join(app.root_path, "uploads")



product_list = [
    {
        "name": "Product Name 1",
        "description": "Product description"
    },
    {
        "name": "Product Name 2",
        "description": "some other description"
    },
    {
        "name": "Cool Product",
        "description": "Product description once more"
    },
    {
        "name": "Bettter Product",
        "description": "Product description again"
    },
    {
        "name": "Best Product",
        "description": "Product description"
    },
]


@app.route("/", methods=["GET", "POST"])
def index():
    form = RegisterForm()

    if form.validate_on_submit():
        file = form.profile_picture.data
        filename, filetype = file.filename.split(".")
        filename = str(uuid4())
        directory = os.path.join(UPLOAD_PATH, f"{filename}.{filetype}")
        file.save(directory)

    if form.errors:
        for errors in form.errors.values():
            for error in errors:
                flash(error)

    return render_template("index.html", user_type="admin", form=form)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/products")
def products():
    return render_template("products.html", prlist=product_list)


@app.route("/products/<int:id>")
def view_product(id):
    chosen_product = product_list[id]
    return render_template("view_product.html", product=chosen_product)


@app.route("/test/<string:name>/<string:surname>")
def test_page(name, surname):
    return f"{name} {surname}"


if __name__ == "__main__":
    app.run()
