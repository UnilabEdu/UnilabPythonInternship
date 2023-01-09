from wtforms.fields import StringField, PasswordField, EmailField, SubmitField, RadioField, BooleanField, SelectField, TextAreaField
from wtforms.validators import DataRequired, length, equal_to, Email
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileSize, FileAllowed, FileRequired


class Registerform(FlaskForm):

    firstname = StringField("Enter your Firstname", render_kw={"class": "form-control"},
                            validators=[DataRequired(message="Firstname is required")])
    lastname = StringField("Enter your Lastname", validators=[DataRequired(
        message="Lastname is required")])
    email = EmailField("Enter your email", validators=[DataRequired(
        message="Email required"), Email(message="Please Enter valid email")])
    writer_experience = RadioField("Which one are you?", choices=[
        (0, "Experienced Writer"), (1, "Begginer Writer")])
    writer_field = SelectField("Field Choices", choices=[
                                   (0, "Personal essay"), (1, "Political essay"), (2,"Compare-and-contrast essay")])
    essay_description = TextAreaField("Send your brief description of your essay")
    essay_file = FileField(validators=[FileAllowed(["pdf","txt"]), FileRequired("Please Upload File")])
    
    submit = SubmitField()
