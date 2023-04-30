from wtforms.fields import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class ProductForm(FlaskForm):

    product_name = StringField(validators=[DataRequired("Product name is required")])
    product_price = FloatField(validators=[DataRequired("Product price is required")])
    product_quantity = FloatField(validators=[DataRequired("Product quantity is required")])

    submit = SubmitField()

