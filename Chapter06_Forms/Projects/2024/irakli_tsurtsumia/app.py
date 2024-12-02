from flask import Flask, render_template, request, redirect
from forms import UserForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "12345678"

data = [
    {"name": "Lizzard", "sale": False, "price": 100, "img": "/static/MainBefore.jpg", "id": 1},
    {"name": "Gizzard", "sale": True, "price": 200, "img": "/static/MainBefore.jpg", "id": 2},
    {"name": "Wizzard", "sale": False, "price": 300, "img": "/static/MainBefore.jpg", "id": 3},
]

users = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/products')
def products():
    return render_template('products.html', products_list=data)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/product/<int:id>')
def product(id):
    return render_template("product.html", product=data[id])


@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    form = UserForm()

    if form.validate_on_submit():
        new_user = {
            "name": form.first_name.data,
            "last_name": form.last_name.data,
            "username": form.username.data,
        }

        users.append(new_user)
        print("users:", users)

        return redirect("/")

    else:
        print("error:", form.errors)

    return render_template("sign_in.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
