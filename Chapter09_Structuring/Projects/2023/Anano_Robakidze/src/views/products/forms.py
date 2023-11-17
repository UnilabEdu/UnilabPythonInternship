from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms.fields import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired



class AddProductForm(FlaskForm):
    category = SelectField('პროდუქტის კატეგორია')
    img = FileField('ატვირთეთ პროდუქტის სურათი', validators=[FileRequired()])
    title = StringField('პროდუქტის სახელი', validators=[DataRequired()])
    color = StringField('პროდუქტის ფერი', validators=[DataRequired()])
    size = SelectField('პროდუქტის ზომა', choices=["S", "M", "L", "XL"])
    price = IntegerField('პროდუქტის ფასი', validators=[DataRequired()])
    submit = SubmitField('დამატება', validators=[DataRequired()])