"""
Routes and views for the web application
"""
from flask import render_template
from Elektronyx.models import *
from Elektronyx.forms import *
from Elektronyx import app

featured_items = (
    GPU.query.filter_by(model="GeForce GTX 1070").first(),
    GPU.query.filter_by(model="GeForce RTX 3090").first(),
    GPU.query.filter_by(model="GeForce GTX 1660 Super").first(),
    CPU.query.filter_by(model="Core i9-10900K").first(),
    CPU.query.filter_by(model="Ryzen 8 2700X").first(),
    Motherboard.query.filter_by(model="ROG STRIX X299-E").first(),
    Motherboard.query.filter_by(model="ROG STRIX Z490-E").first(),
    PSU.query.filter_by(model="ROG Thor 850").first(),
    PSU.query.filter_by(model="HX1000").first(),
    RAM.query.filter_by(model="TridentZ Series").first(),
)

promo_items = (
    ('180.0', Case.find_by_name('Evolv X')),
    ('110.0', Case.find_by_name('H400i')),
    ('149.9', Storage.find_by_name('Barracuda 8TB')),
    ('50.0', Storage.find_by_name('Ultrastar 7K4000'))
)

@app.route('/')
def home():
    return render_template("index.html", featured_items=featured_items, promo_items=promo_items)


@app.route('/catalog/<string:product_type>')
def catalog(product_type):
    if product_type == 'case':
        data = Case.get_all()
    elif product_type == 'motherboard':
        data = Motherboard.get_all()
    elif product_type == "cpu":
        data = CPU.get_all()
    elif product_type == "gpu":
        data = GPU.get_all()
    elif product_type == "psu":
        data = PSU.get_all()
    elif product_type == "ram":
        data = RAM.get_all()
    elif product_type == "storage":
        data = Storage.get_all()

    return render_template("catalog.html", catalog_data=data, product_type=product_type)


@app.route('/catalog/<string:product_type>/<string:product_name>')
def item(product_type, product_name):

    if product_type == 'case':
        data = Case.find_by_name(product_name)
    elif product_type == 'motherboard':
        data = Motherboard.find_by_name(product_name)
    elif product_type == "cpu":
        data = CPU.find_by_name(product_name)
    elif product_type == "gpu":
        data = GPU.find_by_name(product_name)
    elif product_type == "psu":
        data = PSU.find_by_name(product_name)
    elif product_type == "ram":
        data = RAM.find_by_name(product_name)
    elif product_type == "storage":
        data = Storage.find_by_name(product_name)
    
    return render_template("item.html", product=vars(data))


users=[];

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        user_email = form.email.data
        user_password = form.password.data
        users.append([user_email, user_password])

    return render_template('register.html', form=form)
