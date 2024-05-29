from flask import Flask, render_template, request, flash
from forms import RegisterForm,ProductForm

from flask_sqlalchemy import SQLAlchemy
from os import path 
from uuid import uuid4


app =Flask(__name__)
app.config["SECRET_KEY"] = "mystrangesecretkey"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + path.join(app.root_path, "products.db")

db=SQLAlchemy(app)


class Products(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    price = db.Column(db.Integer)
    img = db.Column(db.String)


with app.app_context():
    db.create_all()

@app.route("/add_product",methods = ["GET","POST"])
def add_products():
    form = ProductForm()
    if form.validate_on_submit():
        product = Products(name=form.name.data, price=form.price.data, img =None)
        if form.img.data != None:
         img = form.img.data
         filename, extension = path.splitext(img.filename)
         filename = str(uuid4())
         directory = path.join(app.root_path, "static", "uploads", f"{filename}{extension}")
         img.save(directory)
         product.img = f"{filename}{extension}"
        db.session.add(product)
        db.session.commit()
        flash("წარმატებით დარეგისტრირდით")
    return render_template("add_product.html", form=form)

@app.route("/edit_product/<int:product_id>",methods =["GET","POST"])
def edit_product(product_id):
    product = Products.query.get(product_id)


    if not product:
        flash("პროდუქტი არ მოიძებნა")

    form = ProductForm(obj = product)
    if form.validate_on_submit():
        product.name = form.name.data
        product.price = form.price.data

        if not type (form.img.data)==str:
             
             img = form.img.data
             filename, extension = path.splitext(img.filename)
             filename = str(uuid4())
             directory = path.join(app.root_path, "static", "uploads", f"{filename}{extension}")
             img.save(directory)
             product.img = f"{filename}{extension}"
            
    db.session.commit()
    flash("წარმატებით დარეგისტრირდით")     

    return render_template("add_product.html",form=form)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/materials")
def materials():
    return render_template("materials.html")

@app.route("/products")
def products():
    prod = Products.query.all()
    return render_template("products.html", prod=prod)

@app.route("/products/<int:id>")
def view_product(id):
    product = Products.query.get_or_404(id)  
    return render_template("viewproduct.html", product=product)  


@app.route("/register",methods=["POST","get"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = {"username":form.username.data, 
                    "password":form.password.data, 
                    "repeat_password":form.repeat_password.data, 
                    "age":form.age.data,
                    "gender":form.gender.data,
                    "nationality":form.nationality.data}
        users.append(new_user)
        flash("წარმატებით დარეგისტრირდით")
        print(users)
        img = form.img.data
    return render_template("register.html", form=form)



if __name__ == "__main__":
    app.run(debug=True) 
    db.create_all()