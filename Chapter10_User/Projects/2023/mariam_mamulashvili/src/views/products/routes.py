import os
from uuid import uuid4
from flask import render_template, url_for, Blueprint

from src.models import Product
from src.config import Config

from src.views.products.forms import AddMediaForm

product_blueprint = Blueprint('product', __name__)

@product_blueprint.route('/add_media/', methods=['GET', 'POST'])
def add_media():
    form = AddMediaForm()
    if form.validate_on_submit():
        new_product = Product(
            product_name = form.product_name.data,
            description= form.description.data,
            product_category= form.product_category.data,
            page_category= form.page_category.data)
        

        # FILE UPLOAD
        file = form.product_image.data
        print(file)
        filename, filetype = file.filename.split('.')
        filename = str(uuid4()) 
        directory = os.path.join(Config.UPLOAD_PATH, f"{filename}.{filetype}")
        file.save(directory)
        new_product.image = f"{filename}.{filetype}"
    else:
        print('Form not validated')
    return render_template('products/add_media.html', is_admin=True, form=form)


    