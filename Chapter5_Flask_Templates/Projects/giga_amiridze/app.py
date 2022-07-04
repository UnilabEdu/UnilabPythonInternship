from flask import Flask, render_template
# Resources
from resources.pages import nav_bar_pages
from resources.arrival_products import arrival_products, arrival_title
from resources.seller_products import seller_products, seller_title
from resources.shop_products import shop_products
from resources.magazine_items import magazine_items

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", pages=nav_bar_pages, arrival_items=arrival_products, arrival_title=arrival_title,
                           seller_items=seller_products, seller_title=seller_title)

@app.route('/shop')
def shop():
    return render_template("shop.html", pages=nav_bar_pages, shop_items=shop_products)

@app.route('/press')
def press():
    return render_template("press.html", pages=nav_bar_pages, magazine_items=magazine_items)

if __name__ == "__main__":
    app.run(port=7777, debug=True)