from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired, length, Email, EqualTo
app = Flask(__name__)

app.config['SECRET_KEY'] = "mySECRETkey"


class EmailForm(FlaskForm):
    email = StringField("შეიყვანეთ თქვენი ელ-ფოსტის მისამართი",
                        validators=[
                            DataRequired(),
                            length(min=4),
                            Email(),
                            EqualTo("confirm_email", message="Emails do not match")
                        ]
                        )

    confirm_email = StringField("გაიმეორეთ თქვენი ელ-ფოსტის მისამართი")

    option = RadioField('გთხოვთ აირჩიოთ bending-ის შესაძლებლობა:',
                        choices=[
                            ('sky', 'პირველი პარამეტრი'),
                            ('earth', 'მეორე პარამეტრი'),
                        ]
                        )

    submit = SubmitField("შეყვანა")


@app.route('/', methods=['GET', 'POST'])
def home():
    email = None

    form = EmailForm()

    if form.validate_on_submit():
        email = form.email.data
        option = form.option.data

        print(f"არჩეული პარამეტრია: {option}")

        form.email.data = ''

    return render_template("home.html", form=form, email=email)


if __name__ == '__main__':
    app.run(debug=True)
