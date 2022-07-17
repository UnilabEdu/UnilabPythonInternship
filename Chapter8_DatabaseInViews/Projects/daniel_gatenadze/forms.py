from flask_wtf import FlaskForm
from wtforms.fields import StringField, EmailField, PasswordField, SubmitField, RadioField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf.file import FileField, FileAllowed


class LoginForm(FlaskForm):
    email = EmailField(label="Enter your email",
                       validators=[Email(check_deliverability=False, message="Please Enter Correct Email")],
                       render_kw={"placeholder": "Email"})
    password = PasswordField(label="Enter Password",
                             validators=[DataRequired(message="Please Enter Correct Password"), Length(min=8, max=64)],
                             render_kw={"placeholder": "Password"})
    fileupload = FileField(label="Upload Avatar", validators=[FileAllowed(['.png', '.jpeg', '.PNG', '.JPG'])])
    submit = SubmitField()


class RegisterForm(FlaskForm):
    username = StringField(label="Enter Username",
                           validators=[DataRequired(message="Please Enter Correct Username"), Length(min=8, max=64)],
                           render_kw={"placeholder": "username"})
    email = EmailField(label="Enter your email",
                       validators=[Email(check_deliverability=False, message="Please Enter Correct Email")],
                       render_kw={"placeholder": "email"})
    password = PasswordField(label="Enter Password",
                             validators=[DataRequired(message="Please Enter Correct Password"),
                                         Length(min=8, max=64)], render_kw={"placeholder": "Password"})
    confirmpassword = PasswordField(label="Confirm Password",
                                    validators=[EqualTo("password", message="passwords don't match")],
                                    render_kw={"placeholder": "Confirm Password"})
    gender = RadioField(choices=[("male", "Male"), ("female", "Female"), ("other", "Other")])
    age = IntegerField(label="Age", render_kw={"placeholder": "Age"})
    fileupload = FileField(label="Upload Avatar", validators=[FileAllowed(['png', 'jgp'])])
    submit = SubmitField()


class ProfilePage(FlaskForm):
    textarea = TextAreaField(render_kw={"placeholder": "about"})
