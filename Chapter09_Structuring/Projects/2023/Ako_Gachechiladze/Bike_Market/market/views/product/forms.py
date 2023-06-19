from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, IntegerField, SubmitField


class ProductForm(FlaskForm):
    part = SelectField("Parts", choices=[
        ('bike-forks', 'Fork'),
        ('bike-pedals', 'Pedal'),
        ('handlebars', 'Handlebar'),
        ('bike-wheels', 'Wheels'),
        ('bike-saddles', 'Saddles'),
        ('seatposts', 'Seatpost')
    ])
    name = StringField("Product Name")
    description = StringField("Product Description")
    price = IntegerField("Product Price")
    image = StringField("Product Image")
    submit = SubmitField("Add")


class FilterProductForm(FlaskForm):
    part = SelectField("Parts", choices=[
        ('bike-forks', 'Fork'),
        ('bike-pedals', 'Pedal'),
        ('handlebars', 'Handlebar'),
        ('bike-wheels', 'Wheels'),
        ('bike-saddles', 'Saddles'),
        ('seatposts', 'Seatpost')
    ])
    sort = SelectField("Sorted By", choices=[
        ('loh', 'Low to High'),
        ('hol', 'High to Low')
    ])
    submit = SubmitField("Filter")
    