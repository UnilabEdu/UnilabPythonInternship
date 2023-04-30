from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, length, Email, EqualTo


class EmailForm(FlaskForm):
    name = StringField("Name", validators=[
                            DataRequired()
                        ]
                        )
    email = StringField("Email", validators=[
                            DataRequired()
                        ]
                        )
    text = TextAreaField("Letter", validators=[
                            DataRequired()
                        ]
                        )

    submit = SubmitField("Submit")
