from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms.fields import StringField, IntegerField, SubmitField, SelectField, PasswordField, DateField, RadioField, \
    TextAreaField
from wtforms.validators import DataRequired, length, equal_to, ValidationError
from string import ascii_lowercase, ascii_uppercase, digits


class AddProductForm(FlaskForm):
    product_img_link = FileField('ატვირთეთ პროდუქტის სურათი', validators=[FileRequired()])
    product_title = StringField('პროდუქტის სახელი', validators=[DataRequired()])
    product_color = StringField('პროდუქტის ფერი', validators=[DataRequired()])
    product_size = SelectField('პროდუქტის ზომა', choices=["S", "M", "L", "XL"])
    price = IntegerField('პროდუქტის ფასი', validators=[DataRequired()])
    submit = SubmitField('დამატება', validators=[DataRequired()])


class RegisterForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), length(min=8, max=64)])
    confirm_password = PasswordField('confirm password',
                                     validators=[DataRequired(), equal_to("password", message="პაროლები არ ემთხვევა!")])
    birthday = DateField('birthday', validators=[DataRequired()])
    gender = RadioField('gender', choices=['Male', 'Female', 'Other'])
    about_you = TextAreaField('about you')
    submit = SubmitField('submit')

    def validate_password(self, field):
        contains_uppercase = False
        contains_lowercase = False
        contains_digits = False

        for char in field.data:
            if char in ascii_uppercase:
                contains_uppercase = True

            if char in ascii_lowercase:
                contains_lowercase = True

            if char in digits:
                contains_digits = True

        if not contains_digits or not contains_lowercase or not contains_uppercase:
            raise ValidationError("პაროლი არ აკმაყოფილებს მოთხოვნებს!")


