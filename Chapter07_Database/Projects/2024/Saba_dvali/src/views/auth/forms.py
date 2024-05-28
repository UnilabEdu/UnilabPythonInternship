from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms.fields import StringField, PasswordField, RadioField, DateField, SelectField, TextAreaField, SubmitField, EmailField
from wtforms.validators import DataRequired, equal_to, length, ValidationError
from string import ascii_uppercase, ascii_lowercase, digits, punctuation

    
class LoginForm(FlaskForm):
    username_log = StringField("Username", validators=[DataRequired()])
    password_log = PasswordField("Password", validators=[DataRequired(),
                                                     length(min=8, max=64, message="პაროლი უნდა იყოს მინიმუმ 8 სიმბოლო")])
    submit_log = SubmitField("Log In")
    
 

class RegistrationForm(FlaskForm):
    username_reg = StringField("Username", validators=[DataRequired()])
    email_reg = EmailField("Email", validators=[DataRequired()])

    password_reg = PasswordField("Password", validators=[DataRequired(),
                                                     length(min=8, max=64, message="პაროლი უნდა იყოს მინიმუმ 8 სიმბოლო")])
    # repeat_password_reg = PasswordField("Repeat Password", validators=[DataRequired(),
    #                                                                equal_to("password", message="პაროლები არ ემთხვევა")])
    repeat_password_reg = PasswordField("Password", validators=[DataRequired(),
                                                     length(min=8, max=64, message="პაროლი უნდა იყოს მინიმუმ 8 სიმბოლო")])

    submit_reg = SubmitField("Sign In")


    # def validate_password(self, field):
    #     contains_uppercase = False
    #     contains_lowercase = False
    #     contains_digits = False
    #     contains_symbols = False
    #     for character in field.data:
    #         if character in ascii_uppercase:
    #             contains_uppercase = True

    #         if character in ascii_lowercase:
    #             contains_lowercase = True

    #         if character in digits:
    #             contains_digits = True

    #         if character in punctuation:
    #             contains_symbols = True

    #     if not contains_uppercase:
    #         raise ValidationError("პაროლი უნდა შეიცავდეს დიდ ასოებს")
    #     elif not contains_lowercase:
    #         raise ValidationError("პაროლი უნდა შეიცავდეს პატარა ასოებს")
    #     elif not contains_digits:
    #         raise ValidationError("პაროლი უნდა შეიცავდეს ციფრებს")
    #     elif not contains_symbols:
    #         raise ValidationError("პაროლი უნდა შეიცავდეს სიმბოლოებს")