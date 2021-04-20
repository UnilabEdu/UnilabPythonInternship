"""
Routes and views for the web application
"""
from flask import render_template
from Elektronyx.models import *
from Elektronyx.forms import *
from Elektronyx import app


@app.route('/')
def home():
    return render_template("index.html")


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


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        user_email = form.email.data
        user_password = form.password.data
        users.append([user_email, user_password])

    return render_template('register.html', form=form)
