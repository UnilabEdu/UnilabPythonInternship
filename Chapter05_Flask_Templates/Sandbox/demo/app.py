from flask import Flask, render_template, url_for

app = Flask(__name__)
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


@app.route("/")
def index():
    return render_template("index.html", user_type="admin")


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
