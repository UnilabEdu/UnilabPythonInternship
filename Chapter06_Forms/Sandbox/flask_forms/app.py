from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, DateField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, length, EqualTo
app = Flask(__name__)

app.config["SECRET_KEY"] = "Any kind of secret string"


class SubscriptionForm(FlaskForm):
    username = StringField("* username", [DataRequired(), length(min=4, max=16, message="უნდა გამოიყენოთ 4-16 "
                                                                                        "სიმბოლომდე")])
    password = PasswordField("* password", validators=[DataRequired(),
                                                       length(min=4, max=16, message="უნდა გამოიყენოთ 4-16 სიმბოლომდე"),
                                                       EqualTo('confirm_password', message="პაროლი არ ემთხვევა")])
    confirm_password = PasswordField("* გაიმეორეთ", [DataRequired(),])
    terms_agreement = BooleanField("* ვეთანხმები წესებს", [DataRequired(),])
    subscription_till = DateField("* ჯავშანი", [DataRequired(),])
    type = SelectField(
                        "მომხმარებლის ტიპი",
                        choices=[
                            ('paid', "კომერციული"),
                            ('trial', "დროებითი"),
                            ('vip', "სრული პაკეტი")
                        ]
                    )
    comment = TextAreaField()

    submit = SubmitField("Send")


@app.route('/', methods=['GET', 'POST'])
def home():
    user_input = {}
    form = SubscriptionForm()

    if form.validate_on_submit():
        user_input["user_name"] = form.username.data
        user_input["password"] = form.password.data
        user_input["terms_agreement"] = form.terms_agreement.data
        user_input["subscription_till"] = form.subscription_till.data
        user_input["type"] = form.type.data
        user_input["comment"] = form.comment.data
        # save to db

    return render_template("home.j2", form=form, user_input=user_input)


if __name__ == '__main__':
    app.run(debug=True)
