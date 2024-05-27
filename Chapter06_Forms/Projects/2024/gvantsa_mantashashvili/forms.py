from flask_wtf import FlaskForm
from wtforms.fields import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, length, ValidationError

class RegisterForm(FlaskForm):
    firstname = StringField("სახელი", validators=[DataRequired(),length(min=2, max=24)])
    lastname = StringField("გვარი", validators=[DataRequired(), length(min=2, max=24)])
    email = EmailField("მეილი", validators=[DataRequired(), length(min=5, max=24)])
    password = PasswordField("პაროლი", validators=[DataRequired(), length(min=8, max=24)])

    submit = SubmitField("დარეგისტრირება")

    def validate_password(self, field):
        contain_uppercase = False
        for char in field.data:
            if char in "QWERTYUIOPASDFGHJKLZXCVBNM":
                contain_uppercase = True

        if not contain_uppercase:
            raise ValidationError("პაროლი უნდა შეიცავდეს დიდ ასოებს")


