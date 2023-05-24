from os import path
from uuid import uuid4

from flask import Flask, render_template, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from forms import RegisterForm, ProductForm

BASE_DIRECTORY = path.abspath(path.dirname(__file__))
UPLOAD_PATH = path.join(BASE_DIRECTORY, "uploads")

app = Flask(__name__)
app.config["SECRET_KEY"] = "12345678"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + path.join(BASE_DIRECTORY, "database.db")

db = SQLAlchemy(app)


class Product(db.Model):

    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    price = db.Column(db.Integer)

    def __repr__(self):
        return f"{self.name} (Price: {self.price})"


@app.route("/", methods=["GET", "POST"])
def index():
    form = RegisterForm()

    if form.validate_on_submit():
        file = form.profile_pic.data
        filename, filetype = file.filename.split(".")
        filename = str(uuid4())
        directory = path.join(UPLOAD_PATH, f"{filename}.{filetype}")
        file.save(directory)

    if form.errors:
        for errors in form.errors.items():
            for error in errors:
                flash("SYSTEM ERROR")

    return render_template("index.html", form=form)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/products")
def products():
    product_list = Product.query.all()
    return render_template("products.html", prlist=product_list)


@app.route("/add_product", methods=["GET", "POST"])
def add_product():
    form = ProductForm()

    if form.validate_on_submit():
        new_product = Product(name=form.name.data, description=form.description.data, price=form.price.data)
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('products'))

    return render_template("add_product.html", form=form)


@app.route("/edit_product/<int:id>", methods=["GET", "POST"])
def edit_product(id):
    product = Product.query.get(id)
    form = ProductForm(name=product.name, description=product.description, price=product.price)
    if form.validate_on_submit():
        product.name = form.name.data
        product.description = form.description.data
        product.price = form.price.data
        db.session.commit()
        return redirect(url_for('products'))

    return render_template("add_product.html", form=form)


@app.route("/delete_product/<int:id>")
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()

    return redirect(url_for('products'))


@app.route("/products/<int:id>")
def view_product(id):
    chosen_product = Product.query.get(id)
    return render_template("view_product.html", product=chosen_product)


if __name__ == "__main__":
    app.run(debug=True)
