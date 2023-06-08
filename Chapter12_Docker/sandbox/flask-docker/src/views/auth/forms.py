from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, RadioField, DateField, SelectField, TextAreaField, SubmitField, IntegerField
from wtforms.validators import DataRequired, equal_to, length, ValidationError
from string import ascii_uppercase, ascii_lowercase, digits, punctuation

from src.models import User


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("ავტორიზაცია")


class RegisterForm(FlaskForm):

    username = StringField("Username", validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField("Password", validators=[DataRequired(),
                                                     length(min=8, max=64, message="პაროლი უნდა იყოს მინიმუმ 8 სიმბოლო")])
    repeat_password = PasswordField("Repeat Password", validators=[DataRequired(),equal_to("password", message="პაროლები არ ემთხვევა")])
    gender = RadioField("Gender", choices=["მამრობითი", "მდედრობითი"], validators=[DataRequired("სქესის ველი სავალდებულოა")])
    birthdate = DateField("დაბადების თარიღი", validators=[DataRequired()])

    submit = SubmitField("რეგისტრაცია")

    def validate_username(self, field):
        existing_user = User.query.filter_by(username=field.data).first()
        if existing_user:
            raise ValidationError("ეს იუზერნეიმი უკვე გამოყენებულია")

    def validate_password(self, field):
        contains_uppercase = False
        contains_lowercase = False
        contains_digits = False
        contains_symbols = False
        for character in field.data:
            if character in ascii_uppercase:
                contains_uppercase = True

            if character in ascii_lowercase:
                contains_lowercase = True

            if character in digits:
                contains_digits = True

            if character in punctuation:
                contains_symbols = True

        if not contains_uppercase:
            raise ValidationError("პაროლი უნდა შეიცავდეს დიდ ასოებს")
        elif not contains_lowercase:
            raise ValidationError("პაროლი უნდა შეიცავდეს პატარა ასოებს")
        elif not contains_digits:
            raise ValidationError("პაროლი უნდა შეიცავდეს ციფრებს")
        elif not contains_symbols:
            raise ValidationError("პაროლი უნდა შეიცავდეს სიმბოლოებს")