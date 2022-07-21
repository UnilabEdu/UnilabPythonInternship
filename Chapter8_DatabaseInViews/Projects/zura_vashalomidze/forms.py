from flask_wtf import FlaskForm
from wtforms.fields import StringField, EmailField, PasswordField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Email


class LoginForm(FlaskForm):
    login = StringField(label="Name:", validators=[DataRequired()])
    email = EmailField(label="Email address:", validators=[Email()])
    password = PasswordField(label="Password:")
    confirmpassword = PasswordField(label=" Confirm Password:", validators=[EqualTo("password", message="password "
                                                                                                       "don't match")])
    message = TextAreaField(label="Message")

    submit = SubmitField(label="Submit")


class DelForm(FlaskForm):
    id = IntegerField('Id Number of Student to Remove:')
    name = StringField("Name of Student to Remove")
    submit = SubmitField('Remove Student')
