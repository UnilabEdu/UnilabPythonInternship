from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, RadioField, DateField, SelectField, TextAreaField, SubmitField, \
    IntegerField
from wtforms.validators import DataRequired, equal_to, length, ValidationError
from string import ascii_lowercase, ascii_letters, ascii_uppercase, digits, punctuation


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), length(min=4, max=88, message="min length is four")])
    second_pass = PasswordField('Repeat Pass', validators=[DataRequired(), equal_to("password")])

    gender = RadioField('Gender', choices=["Female", "Male"])
    birthday = DateField('BirthDay')
    country = SelectField('Select Country', choices=[ (None, "Select"), ("gruzia", "GEO"), ("rusia", "RUS"), ("england", "ENG")])
    about_me = TextAreaField('AboutMe')
    profile_pic = FileField()
    submit = SubmitField('Submit')

    def validate_password(self, field):

        uppercase = False
        lowercase = False
        passdigits = False
        passsymbols = False

        for character in field.data:
            if character in ascii_uppercase:
                uppercase = True
            if character in ascii_lowercase:
                lowercase = True
            if character in digits:
                passdigits = True
            if character in punctuation:
                passsymbols = True

        if not uppercase:
            raise ValidationError("Password Need Large Letters")
        elif not lowercase:
            raise ValidationError("Password Need Small Letters")
        elif not passdigits:
            raise ValidationError("Password Need Digit Letters")
        elif not passsymbols:
            raise ValidationError("Password Need Symbol Letters")


class ProductForm(FlaskForm):

    name = StringField("პროდუქტის სახელი")
    description = TextAreaField("პროდუქტის აღწერა")
    price = IntegerField("პროდუქტის ფასი")

    submit = SubmitField("ცვლილება")