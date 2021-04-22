from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, PasswordField, IntegerField
from wtforms.validators import DataRequired, length, Email, EqualTo
from wtforms import ValidationError
from app.models import Student


class EmailFormStudent(FlaskForm):
    username = StringField("Enter your name:", validators=[DataRequired(), length(min=2, max=15)])

    email = StringField("Enter your email:",
                        validators=[
                            DataRequired(),
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

    tutor_id = StringField("Enter your tutor's id")

    submit = SubmitField("Submit")

    def validate_email_from_db(self, email):
        temp_email = self.email.data
        if Student.find_by_email(temp_email):
            raise ValidationError("Email already exists")


class LoginFormStudent(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField("Log in")
