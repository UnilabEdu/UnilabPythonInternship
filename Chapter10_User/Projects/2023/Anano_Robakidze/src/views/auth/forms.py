from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, PasswordField, DateField, RadioField, \
    TextAreaField
from wtforms.validators import DataRequired, length, equal_to, ValidationError
from string import ascii_lowercase, ascii_uppercase, digits




class RegisterForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), length(min=8, max=64)])
    confirm_password = PasswordField('confirm password',
                                     validators=[DataRequired(), equal_to("password", message="პაროლები არ ემთხვევა")])
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
            raise ValidationError("პაროლი არ აკმაყოფილებს მოთხოვნებს")



class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), length(min=8, max=64)])
    login = SubmitField("Login")
