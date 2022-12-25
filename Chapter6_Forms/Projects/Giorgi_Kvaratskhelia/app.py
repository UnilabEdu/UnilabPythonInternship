from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, length, Email, EqualTo
from resources import item_dictionary


app = Flask(__name__)
app.config['SECRET_KEY'] = "ayylmao"

users = []


class RegisterForm(FlaskForm):

    email = StringField("Enter your E-Mail",validators=[DataRequired(),Email()])
    password = PasswordField("Enter your password",validators=[DataRequired(),length(min=6), EqualTo('confirmpassword', message='Passwords must match')])
    confirmpassword = PasswordField("Confirm your password")
    submit = SubmitField("Register")


@app.route('/')
def display_home_page():
    return render_template("index.html")


@app.route('/catalog/<string:product_type>')
def display_catalog_page(product_type):
    data = item_dictionary[product_type]
    return render_template("catalog.html", catalog_data=data, product_type=product_type)


@app.route('/catalog/<string:product_type>/<string:product_name>')
def display_item_page(product_type, product_name):
    for product in item_dictionary[product_type]:
        if product_name in product['model']:
            item_data = product
            return render_template("item.html", product=item_data)


@app.route('/register', methods=['GET', 'POST'])
def registration_page():

    form = RegisterForm()

    if form.validate_on_submit():
        user_username = form.username.data
        user_email = form.email.data
        user_password = form.password.data
        users.append([user_email, user_password])

    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run()