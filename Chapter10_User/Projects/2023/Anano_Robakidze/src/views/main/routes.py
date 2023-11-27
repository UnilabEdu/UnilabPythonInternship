from flask import render_template, Blueprint

from src.models import Product



main_blueprint = Blueprint("main", __name__)

@main_blueprint.route('/')
@main_blueprint.route('/home')
def home():
    products = Product.query.all()
    return render_template('main/product_list.html', products=products)



@main_blueprint.route('/about_page')
def about():
    return render_template('main/about.html')


