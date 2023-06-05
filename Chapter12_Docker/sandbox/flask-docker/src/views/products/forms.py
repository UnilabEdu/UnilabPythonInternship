from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField, TextAreaField, SubmitField

class ProductForm(FlaskForm):

    name = StringField("პროდუქტის სახელი")
    description = TextAreaField("პროდუქტის აღწერა")
    price = IntegerField("პროდუქტის ფასი")

    submit = SubmitField("პროდუქტის დამატება")