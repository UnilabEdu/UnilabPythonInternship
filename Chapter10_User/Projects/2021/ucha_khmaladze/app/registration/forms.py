from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, length, Email, EqualTo

class RegisterForm(FlaskForm):

    name = StringField("First name", validators=[DataRequired()], render_kw={'placeholder':'e.g john'})
    last_name = StringField("First name", validators=[DataRequired()], render_kw={'placeholder':'e.g smith'})
    email = StringField("Email", validators=[DataRequired(),
                                             length(min=5),
                                             Email(message="Wrong format!")
                                             ])
    password = PasswordField("Password", validators=[DataRequired(), EqualTo("rep_password")])
    rep_password = PasswordField("Repeat password", validators=[DataRequired()])
    submit = SubmitField("Register")