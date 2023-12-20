from flask import render_template, Blueprint, abort, redirect, url_for
from flask_login import login_user, logout_user

main_blueprint = Blueprint('main', __name__)

from src.models import Product, Works

@main_blueprint.route('/')
def home():
    films = Works.query.all()
    return render_template('main/home.html', is_admin=True, films = films)

@main_blueprint.route('/gallery/<string:page_category>')
def gallery(page_category):
    products_image = Product.query.filter(Product.page_category == page_category).all()
    return render_template('main/gallery.html', products_image = products_image)

@main_blueprint.route('/gimbal/<string:page_category>/<string:product_category>')
def gimbal(page_category, product_category):
    products_image = Product.query.filter(Product.page_category == page_category, Product.product_category == 'image').all()
    products_video = Product.query.filter(Product.page_category == page_category, Product.product_category == 'video').all()
    return render_template('main/gimbal.html',  products_image=products_image, products_video=products_video)

@main_blueprint.route('/atmospherics/<string:page_category>/<string:product_category>')
def atmospherics(page_category, product_category):
    products_image = Product.query.filter(Product.page_category == page_category, Product.product_category == 'image').all()
    products_video = Product.query.filter(Product.page_category == page_category, Product.product_category == 'video').all()
    return render_template('main/atmospherics.html', products_image=products_image, products_video=products_video)

@main_blueprint.route('/prosthetics/<string:page_category>/<string:product_category>')
def prosthetics(page_category, product_category):
    products_image = Product.query.filter(Product.page_category == page_category, Product.product_category == 'image').all()
    products_video = Product.query.filter(Product.page_category == page_category, Product.product_category == 'video').all()
    return render_template('main/prosthetics.html', products_image=products_image, products_video=products_video)

@main_blueprint.route('/pyrotechnics/<string:page_category>/<string:product_category>')
def pyrotechnics(page_category, product_category):
    products_image = Product.query.filter(Product.page_category == page_category, Product.product_category == 'image').all()
    products_video = Product.query.filter(Product.page_category == page_category, Product.product_category == 'video').all()
    return render_template('main/pyrotechnics.html',  products_image=products_image, products_video=products_video)

@main_blueprint.route('/model_making/<string:page_category>/<string:product_category>')
def model_making(page_category, product_category):
    products_image = Product.query.filter(Product.page_category == page_category, Product.product_category == 'image').all()
    products_video = Product.query.filter(Product.page_category == page_category, Product.product_category == 'video').all()
    return render_template('main/model_making.html',  products_image=products_image, products_video=products_video)

@main_blueprint.route('/about/')
def about():
    return render_template('main/about.html')

@main_blueprint.route('/works/')
def works():
    films = Works.query.all()
    return render_template('main/works.html',  films=films)

@main_blueprint.route('/works/<string:product_name>')
def view_works(product_name):
    film = Works.query.filter_by(product_name=product_name).first()

    if film:
        return render_template('main/view_works.html', film=film)
    else:
        abort(404)

@main_blueprint.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('main.home'))
