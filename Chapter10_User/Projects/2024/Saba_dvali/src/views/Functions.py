from flask import request
import os
from werkzeug.utils import secure_filename
from flask_login import login_user, current_user


from src.models import Products
from src.views.auth.forms import AddProductForm
from src.ext import db
from src.config import Config


def add_product():
    form = AddProductForm()
    if form.validate_on_submit():
        product_name =  form.product_name.data
        product_model =  form.product_model.data
        price =  str(form.price.data)
        info =  form.info.data

        addproduct = Products(product_name=product_name,
                            product_model=product_model,
                            price=price,
                            info=info,
                            user_id=current_user.id)
        db.session.add(addproduct)
        db.session.commit()
        product = db.session.query(Products).filter(Products.product_name == product_name,
                                                    Products.product_model == product_model,
                                                    Products.price == price,
                                                    Products.info == info,
                                                    Products.user_id == current_user.id
                                                    ).first()
        if product:
            product_images = request.files.getlist('product_images')
            product_dir = os.path.join(f"{Config.PROJECT_ROOT}/static/images", str(product.id))
            if not os.path.exists(product_dir):
                os.makedirs(product_dir)
                for file in product_images:
                    if file.filename != '':
                        filename = secure_filename(file.filename)
                        file.save(os.path.join(product_dir, filename))
                        img = Images(image_name=filename,product_id=product.id)
                db.session.add(img)
                db.session.commit()