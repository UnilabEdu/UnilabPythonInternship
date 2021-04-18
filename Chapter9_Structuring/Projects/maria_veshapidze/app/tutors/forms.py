from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, PasswordField, IntegerField
from wtforms.validators import DataRequired, length, Email, EqualTo


class EmailFormTutor(FlaskForm):
    name = StringField("Enter your name:", [DataRequired(), length(min=2, max=15)])

    email = StringField("Enter your email:",
                        validators=[
                            DataRequired(),
                            length(min=4),
                            Email()
                        ]
                        )

    password = PasswordField("Enter a password:",
                             validators=[
                                 DataRequired(),
                                 length(min=6),
                                 EqualTo("confirm_password", message="Passwords do not match")
                             ]
                             )

    confirm_password = PasswordField("Reenter a password:")

    subject = StringField("Enter a subject:", [DataRequired(), length(min=2, max=15)])

    submit = SubmitField("Submit")
