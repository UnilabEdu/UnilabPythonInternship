from flask import Flask, render_template, redirect, url_for
from form import AddProductForm, RegisterForm
from uuid import uuid4
import os

app = Flask(__name__, template_folder='templates')
app.config["SECRET_KEY"] = "abjdlhrjekls78akkjlllakqawss"
UPLOAD_PATH = os.path.join(app.root_path, "static", "img")

product_list = [
    {"name": "Shirt", "color": "red", "size": "S", "img": "apparel-162192_1280.png", "price": 100},
    {"name": "Shoes", "color": "brown", "size": "M", "img": "clothes-1295223_1280.png", "price": 250},
    {"name": "Coat Jacket", "color": "grey", "size": "M", "img": "coat-30208_1280.png", "price": 200},
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('product_list.html', products=product_list)


@app.route('/product/<int:id>')
def product(id):
    product_id = product_list[id]
    return render_template('product.html', product=product_id)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/add_product', methods=["GET", "POST"])
def add_product():
    form = AddProductForm()
    if form.validate_on_submit():
        # upload file
        file = form.product_img_link.data
        filename, filetype = file.filename.split(".")
        filename = str(uuid4())
        directory = os.path.join(UPLOAD_PATH, f"{filename}.{filetype}")
        file.save(directory)

        product_dict = {
            "name": form.product_title.data,
            "color": form.product_color.data,
            "size": form.product_size.data,
            "img": f"{filename}.{filetype}",
            "price": form.price.data
        }
        product_list.append(product_dict)

        return redirect(url_for('home'))

    return render_template('add_product.html', form=form)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))

    return render_template('register.html', form=form)


@app.route('/edit_product/<int:id>', methods=["GET", "POST", "PUT"])
def edit_product(id):
    product = product_list[id]
    form = AddProductForm(product_title=product['name'], product_img_link=product['img'],
                          product_color=product['color'], product_size=product['size'], price=product['price'])
    if form.validate_on_submit():
        # upload file
        file = form.product_img_link.data
        filename, filetype = file.filename.split(".")
        filename = str(uuid4())
        directory = os.path.join(UPLOAD_PATH, f"{filename}.{filetype}")
        file.save(directory)

        product['name'] = form.product_title.data
        product['img'] = f"{filename}.{filetype}"
        product['color'] = form.product_color.data
        product['size'] = form.product_size.data
        product['price'] = form.price.data

        return redirect(url_for('home'))

    return render_template('edit_product.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)