from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
import re


class RegisterForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    email_address = StringField("Email Address", validators=[DataRequired(), Email()])
    phone_number = StringField("Phone Number", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired()])
    terms_and_conditions = BooleanField("Terms and Conditions")
    submit = SubmitField("Sign Up")

    def validate_password(self, field):
        contains_lowercase = re.compile(r".*[a-z].*")
        contains_uppercase = re.compile(r".*[A-Z].*")
        contains_digits = re.compile(r".*[0-9].*")
        contains_symbol = re.compile(r".*[^\s0-9a-zA-Z].*")
        contain_validators = [contains_lowercase, contains_uppercase, contains_digits, contains_symbol]
        if not all([validator.search(field.data) for validator in contain_validators]):
            raise ValidationError("Stronger password needed (must contain: uppercase, lowercase, digit and symbol character).")

    def validate_confirm_password(self, field):
        if field.data != self.password.data:
            raise ValidationError("Passwords does not match.")


    def validate_phone_number(self, field):
        phone_number_compiler = re.compile(r'''^\s*
                   (\+\d{1,3}(\s|-|))?     # Lets user use regional code
                   \d{3}(\s|-|)            # First 3 digits Delimeters can be - '-'; ' ' or ''
                   ((\d{2}(\s|-|)){2}      # First format where you can section numbers dividing by 2 digits
                   \d{2}|
                   \d{3}(\s|-|)\d{3})      # Second format where you can section numbers dividing by 3 digits
                   \s*                     # Last 2 digits
                   $''', re.VERBOSE, )
        if not phone_number_compiler.search(field.data):
            raise ValidationError(f"Invalid phone number.")


    def validate_terms_and_conditions(self, field):
        if not field.data:
            raise ValidationError(f"You must accept terms and conditions.")

class LoginForm(FlaskForm):
    email_address = StringField("Email")
    password = PasswordField("Password")
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Log In")


class AddBookForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    submit = SubmitField("Add book")
