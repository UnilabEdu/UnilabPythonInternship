from flask import Flask, render_template, request, flash
from forms import RegisterForm
from data import prod_list,users
from flask_sqlalchemy import SQLAlchemy
app =Flask(__name__)
app.config["SECRET_KEY"] = "mystrangesecretkey"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///products.db"


db=SQLAlchemy(app)
class Products(db.Model):
    __tablename_ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Integer)


with app.app_context():
    db.create_all()


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
    print("hi")
    return render_template("products.html", prod=prod_list)

@app.route("/products/<int:id>")
def view_product(id):
   # picked_product= prod_list[id]
    return render_template("viewproduct.html",specprod=prod_list[id])

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
        
    return render_template("register.html", form=form)



if __name__ == "__main__":
    app.run(debug=True)