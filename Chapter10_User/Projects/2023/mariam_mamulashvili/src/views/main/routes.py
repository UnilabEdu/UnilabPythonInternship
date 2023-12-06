from flask import render_template, Blueprint, abort

main_blueprint = Blueprint('main', __name__)

from src.models import Product, Works

@main_blueprint.route('/')
def home():
    return render_template('main/home.html', is_admin=True)

@main_blueprint.route('/gimbal/<string:page_category>/<string:product_category>')
def gimbal(page_category, product_category):
    products_image = Product.query.filter(Product.page_category == page_category, Product.product_category == 'image').all()
    products_video = Product.query.filter(Product.page_category == page_category, Product.product_category == 'video').all()
    return render_template('main/gimbal.html', is_admin=True, products_image=products_image, products_video=products_video)

@main_blueprint.route('/atmospherics/<string:page_category>/<string:product_category>')
def atmospherics(page_category, product_category):
    products_image = Product.query.filter(Product.page_category == page_category, Product.product_category == 'image').all()
    products_video = Product.query.filter(Product.page_category == page_category, Product.product_category == 'video').all()
    return render_template('main/atmospherics.html', is_admin=True, products_image=products_image, products_video=products_video)

@main_blueprint.route('/prosthetics/<string:page_category>/<string:product_category>')
def prosthetics(page_category, product_category):
    products_image = Product.query.filter(Product.page_category == page_category, Product.product_category == 'image').all()
    products_video = Product.query.filter(Product.page_category == page_category, Product.product_category == 'video').all()
    return render_template('main/prosthetics.html', is_admin=True, products_image=products_image, products_video=products_video)

@main_blueprint.route('/pyrotechnics/<string:page_category>/<string:product_category>')
def pyrotechnics(page_category, product_category):
    products_image = Product.query.filter(Product.page_category == page_category, Product.product_category == 'image').all()
    products_video = Product.query.filter(Product.page_category == page_category, Product.product_category == 'video').all()
    return render_template('main/pyrotechnics.html', is_admin=True, products_image=products_image, products_video=products_video)

@main_blueprint.route('/model_making/<string:page_category>/<string:product_category>')
def model_making(page_category, product_category):
    products_image = Product.query.filter(Product.page_category == page_category, Product.product_category == 'image').all()
    products_video = Product.query.filter(Product.page_category == page_category, Product.product_category == 'video').all()
    return render_template('main/model_making.html', is_admin=True, products_image=products_image, products_video=products_video)

@main_blueprint.route('/about/')
def about():
    return render_template('main/about.html', is_admin=True)

@main_blueprint.route('/works/')
def works():
    films = Works.query.all()
    return render_template('main/works.html', is_admin=True, films=films)

@main_blueprint.route('/works/<string:product_name>')
def view_works(product_name):
    film = Works.query.filter_by(product_name=product_name).first()

    if film:
        return render_template('main/view_works.html', film=film, is_admin=True)
    else:
        abort(404)
