from flask_wtf import FlaskForm
from wtforms.fields import StringField, SelectField , IntegerField , SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, length, ValidationError
from string import ascii_lowercase, ascii_uppercase, digits

class AddUser(FlaskForm):
    user_name = StringField("Name", validators=[DataRequired(),length(min=8, max=64)])
    user_surname = StringField("Surname", validators=[DataRequired(), length(min=8, max=64)])
    user_email = EmailField("Email", validators=[DataRequired()])
    user_password = PasswordField("Password", validators=[DataRequired()])
    user_submit = SubmitField("Submit")

    def validate_user_password(self,field):
        contains_uppercase = False
        contains_lowercase = False
        contains_digits = False

        for character in field.data:
            if character in ascii_uppercase:
                contains_uppercase = True

            if character in digits:
                contains_digits = True
        if not contains_digits and contains_uppercase:
            raise ValidationError("Uppercase and Digits needed")

class LogUser(FlaskForm):
    loguser_email = EmailField("Email", validators=[DataRequired()])
    loguser_password = PasswordField("Password", validators=[DataRequired()])
    loguser_submit = SubmitField("Submit")


