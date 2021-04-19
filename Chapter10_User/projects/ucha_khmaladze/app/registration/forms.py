from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, length, Email

class RegisterForm(FlaskForm):

    name = StringField("First name", validators=[DataRequired()], render_kw={'placeholder':'e.g john'})
    last_name = StringField("First name", validators=[DataRequired()], render_kw={'placeholder':'e.g smith'})
    email = StringField("Email", validators=[DataRequired(),
                                             length(min=5),
                                             Email(message="Wrong format!")
                                             ])
    password = StringField("Password")
    rep_password = StringField("Repeat password")
    submit = SubmitField("Register")