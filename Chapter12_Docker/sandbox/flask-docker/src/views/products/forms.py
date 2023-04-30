from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField, SubmitField


class ProductForm(FlaskForm):

    product_name = StringField("Product Name")
    product_category = StringField("Product Category")
    price = IntegerField("Product Price")

    submit = SubmitField()