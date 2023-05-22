from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy

from forms import RegisterForm, ProductForm
from os import path
from uuid import uuid4

BASE_DIRECTORY = path.abspath(path.dirname(__file__))
UPLOAD_PATH = path.join(BASE_DIRECTORY, "uploads")

app = Flask(__name__)
app.config["SECRET_KEY"] = "kljadskl10248120318znx"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + path.join(BASE_DIRECTORY, "database.db")

db = SQLAlchemy(app)


######################################
##             MODELS               ##
######################################
class Product(db.Model):

    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    price = db.Column(db.Integer)

    def __repr__(self):
        return f"{self.name} (Price: {self.price})"


# ONE - TO - ONE relationship
class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    birthdate = db.Column(db.Date)

    idcard_id = db.Column(db.ForeignKey("id_cards.id"))
    idcard = db.relationship("IDCard", back_populates="user")

    def __repr__(self):
        return f"{self.name} {self.surname}"


class IDCard(db.Model):
    __tablename__ = "id_cards"

    id = db.Column(db.Integer, primary_key=True)
    id_number = db.Column(db.String, unique=True)
    creation_date = db.Column(db.Date)
    expiry_date = db.Column(db.Date)

    user = db.relationship("User", back_populates="idcard")

    def __repr__(self):
        return f"პირადობა, ნომრით {self.id_number}"


# ONE - TO - MANY Relationship
class University(db.Model):

    __tablename__ = "universities"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    students = db.relationship("Student", back_populates="university")

    def __repr__(self):
        return f"{self.name}"


class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    faculty = db.Column(db.String)

    university_id = db.Column(db.ForeignKey("universities.id"))
    university = db.relationship("University", back_populates="students")

    def __repr__(self):
        return f"{self.name} {self.surname}"


# MANY - TO - MANY Relationship
class Actor(db.Model):
    __tablename__ = "actors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    networth = db.Column(db.String)

    movies = db.relationship("Movie", secondary="movies_actors", back_populates="actors")

    def __repr__(self):
        return f"{self.name} {self.surname}"


class MovieActor(db.Model):

    __tablename__ = "movies_actors"

    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"))
    actor_id = db.Column(db.Integer, db.ForeignKey("actors.id"))


class Movie(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    genre = db.Column(db.String)

    actors = db.relationship("Actor", secondary="movies_actors", back_populates="movies")

    def __repr__(self):
        return f"{self.name}"


######################################
##              ROUTES              ##
######################################
@app.route("/", methods=["GET", "POST"])
def index():
    form = RegisterForm()

    if form.validate_on_submit():
        file = form.profile_picture.data
        filename, filetype = file.filename.split(".")
        filename = str(uuid4())
        directory = path.join(UPLOAD_PATH, f"{filename}.{filetype}")
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

    flash("პროდუქტი წაიშალა")
    return redirect(url_for('products'))


@app.route("/products/<int:id>")
def view_product(id):
    chosen_product = Product.query.get(id)
    return render_template("view_product.html", product=chosen_product)


@app.route("/test/<string:name>/<string:surname>")
def test_page(name, surname):
    return f"{name} {surname}"


if __name__ == "__main__":
    app.run(debug=True)
