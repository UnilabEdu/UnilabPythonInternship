from flask import render_template, Blueprint

main_blueprint = Blueprint('main', __name__)

from src.models import Product

@main_blueprint.route('/')
def home():
    product = Product.query.all()
    return render_template('main/home.html', is_admin=True)

@main_blueprint.route('/gimbal/')
def gimbal():
    product = Product.query.all()
    return render_template('main/gimbal.html', is_admin=True, products=product)

@main_blueprint.route('/atmospherics/')
def atmospherics():
    product = Product.query.all()
    return render_template('main/atmospherics.html', is_admin=True, products=product)

@main_blueprint.route('/prosthetics/')
def prosthetics():
    product = Product.query.all()
    return render_template('main/prosthetics.html', is_admin=True, products=product)

@main_blueprint.route('/pyrotechnics/')
def pyrotechnics():
    product = Product.query.all()
    return render_template('main/pyrotechnics.html', is_admin=True, products=product)

@main_blueprint.route('/model_making/')
def model_making():
    product = Product.query.all()
    return render_template('main/model_making.html', is_admin=True, products=product)

@main_blueprint.route('/about/')
def about():
    return render_template('main/about.html', is_admin=True)

@main_blueprint.route('/works/')
def works():
    product = Product.query.all()
    return render_template('main/works.html', is_admin=True)

