from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField


from flask_wtf.file import FileField


class ProductForm(FlaskForm):
    name = StringField("პროდუქტის სახელი")
    price = IntegerField("შეიყვანეთ ფასი")
    img = FileField()

    submit = SubmitField()