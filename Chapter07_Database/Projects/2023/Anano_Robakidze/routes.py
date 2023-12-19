from app import app, UPLOAD_PATH
from flask import redirect, render_template, url_for, request
from form import AddProductForm, RegisterForm
from models import Product, ProductCategory
from uuid import uuid4
import os


@app.route('/')
@app.route('/home')
def home():
    products = Product.query.all()
    return render_template('product_list.html', products=products)


@app.route('/product/<int:category_id>/<int:id>')
def product(category_id, id):
    product_id = Product.query.get(id)
    return render_template('product.html', product=product_id)


@app.route('/category/<int:category_id>')
def category(category_id):
    select_category = ProductCategory.query.get(category_id)
    products = select_category.products

    return render_template('product_list.html', products=products)



@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/add_product', methods=["GET", "POST"])
def add_product():
    form = AddProductForm()
    categories = ProductCategory.query.all()
    form.category.choices = [(category.id, category.title) for category in categories]

    if form.validate_on_submit():
        new_product = Product()

        new_product.title = form.title.data
        new_product.color = form.color.data
        new_product.size = form.size.data
        new_product.price = form.price.data

        #form.populate_obj(new_product)

        # Set the category_id before saving
        new_product.category_id = form.category.data

        # upload file
        file = form.img.data
        filename, filetype = file.filename.split(".")
        filename = str(uuid4())
        directory = os.path.join(UPLOAD_PATH, f"{filename}.{filetype}")
        file.save(directory)

        new_product.img = f"{filename}.{filetype}"

        new_product.create()

        return redirect(url_for('home'))

    return render_template('add_product.html', form=form)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))

    return render_template('register.html', form=form)


@app.route('/edit_product/<int:category_id>/<int:id>', methods=["GET", "POST", "PUT"])
def edit_product(category_id, id):
    product = Product.query.get(id)
    form = AddProductForm(obj=product)

    categories = ProductCategory.query.all()
    form.category.choices = [(category.id, category.title) for category in categories]

    if form.validate_on_submit():
        # Update product attributes from form data
        product.title = form.title.data
        product.color = form.color.data
        product.size = form.size.data
        product.price = form.price.data

        # Fetch the ProductCategory instance
        selected_category = ProductCategory.query.get(form.category.data)

        # Assign the category to the product
        product.category = selected_category
        product.category_id = selected_category.id  # Set category_id

        # Upload file if a new one is provided
        file = form.img.data
        if file:
            filename, filetype = file.filename.split(".")
            filename = str(uuid4())
            directory = os.path.join(UPLOAD_PATH, f"{filename}.{filetype}")
            file.save(directory)
            product.img = f"{filename}.{filetype}"

        product.save()
        return redirect(url_for('home'))

    return render_template('edit_product.html', form=form)