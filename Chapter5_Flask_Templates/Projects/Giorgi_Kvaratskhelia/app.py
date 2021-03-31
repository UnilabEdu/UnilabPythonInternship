from flask import Flask, render_template
from resources import item_dictionary

app = Flask(__name__)


@app.route('/')
def display_home_page():
    return render_template("index.html")


@app.route('/catalog/<string:product_type>')
def display_catalog_page(product_type):
    data = item_dictionary[product_type]
    return render_template("catalog.html", catalog_data=data)


if __name__ == '__main__':
    app.run()