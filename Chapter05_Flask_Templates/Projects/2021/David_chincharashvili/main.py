from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, length, Email
import requests
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = "this_is_secret_key"


class FormName(FlaskForm):
    name = StringField("Name")
    email = StringField("Email", [DataRequired(), length(max=100, min=5), Email("Field should be real Email")])
    textarea = TextAreaField("Message", [DataRequired(), length( min=5)])
    submit = SubmitField("Send")


@app.route('/')
def home():
    return render_template('page.html')


@app.route('/about_us')
def about():
    resp = requests.get("https://jsonplaceholder.typicode.com/users")
    data=json.loads(resp.text)
    return render_template('about.html', data=data)


@app.route('/contact_us', methods=['GET', 'POST'])
def contact():
    form = FormName(request.form)
    if form.validate_on_submit():
        email = form.email.data
        name = form.name.data
        textarea = form.textarea.data
    return render_template('contact.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)