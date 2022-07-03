from flask import Flask, render_template
# Resources
from resources.pages import pages
from resources.arrival_products import arrival_products

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", pages=pages, items=arrival_products)

@app.route('/shop')
def shop():
    return render_template("shop.html", pages=pages)

@app.route('/press')
def press():
    return render_template("press.html", pages=pages)

if __name__ == "__main__":
    app.run(port=7777, debug=True)