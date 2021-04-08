from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired, length, Email, EqualTo

app = Flask(__name__)

app.config['SECRET_KEY'] = "mySECRETkey"


class EmailForm(FlaskForm):

    name = StringField("შეიყვანეთ თქვენი სახელი", [DataRequired(), length(min=2, max=15)])

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
                            ('air', 'ჰაერი'),
                            ('earth', 'მიწა'),
                            ('fire', 'ცეცხლი'),
                            ('water', 'წყალი'),
                        ]
                        )

    submit = SubmitField("შეყვანა")


@app.route('/', methods=['GET', 'POST'])
def home():
    email = None

    form = EmailForm()

    if form.validate_on_submit():
        session['name'] = form.name.data
        session['email'] = form.email.data
        session['option'] = form.option.data

        return redirect(url_for('thank_you_page'))

    return render_template("home.html", form=form, email=email)


@app.route('/thank_you_page')
def thank_you_page():
    return render_template("thanks.html")

if __name__ == '__main__':
    app.run(debug=True)
