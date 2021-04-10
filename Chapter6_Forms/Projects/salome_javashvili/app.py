from flask import Flask, render_template, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired, Email, length

app = Flask(__name__)

app.config['SECRET_KEY'] = "mySeCrEtKey"

class EmailForm(FlaskForm):
    email = StringField("შეიყვანეთ ელ-ფოსტა")
    option = RadioField("აირჩიეთ:",
                        choices=[
                            ("1", "გიყვარვარ"),
                            ("2", "გკიდივარ")
                        ]
                        )
    submit = SubmitField("გაგზავნა")


app.route("/"):
def home():
    pass

app.route("/thank_you"):
def ty():
    pass


if __name__ == '__main__':
    app.run(debug=True)
