from app import flask_app, UPLOAD_PATH
from flask import render_template, url_for
from db import db
from forms import AddMediaForm, ContactForm

from models import Product

import os
from uuid import uuid4

is_admin = True

product_dictionary = []

@flask_app.route('/')
def home():
    product = Product.query.all()
    return render_template('home.html', is_admin=is_admin)

@flask_app.route('/gimbal/')
def gimbal():
    return render_template('gimbal.html', is_admin=is_admin, product_dictionary=product_dictionary)

@flask_app.route('/atmospherics/')
def atmospherics():
    return render_template('atmospherics.html', is_admin=is_admin, product_dictionary=product_dictionary)

@flask_app.route('/prosthetics/')
def prosthetics():
    return render_template('prosthetics.html', is_admin=is_admin, product_dictionary=product_dictionary)

@flask_app.route('/pyrotechnics/')
def pyrotechnics():
    return render_template('pyrotechnics.html', is_admin=is_admin, product_dictionary=product_dictionary)

@flask_app.route('/model_making/')
def model_making():
    return render_template('model_making.html', is_admin=is_admin, product_dictionary=product_dictionary)

@flask_app.route('/about/')
def about():
    product = Product.query.all()
    return render_template('about.html', is_admin=is_admin)

@flask_app.route('/add_media/', methods=['GET', 'POST'])
def add_media():
    form = AddMediaForm()
    if form.validate_on_submit():
        new_product = Product(
            name = form.product_name.data,
            description= form.description.data,
            product_category= form.product_category.data,
            page_category= form.page_category.data)
        
        

        # FILE UPLOAD
        file = form.product_image.data
        print(file)
        filename, filetype = file.filename.split('.')
        filename = str(uuid4()) 
        directory = os.path.join(UPLOAD_PATH, f"{filename}.{filetype}")
        file.save(directory)
        new_product.image = f"{filename}.{filetype}"
        db.session.add(new_product)
        db.session.commit()
    else:
        print('Form not validated')
    return render_template('add_media.html', is_admin=is_admin, form=form)


@flask_app.route('/contact/', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        print('Form validated')
    print(url_for('contact'))
    return render_template('contact.html', is_admin=is_admin, form=form)