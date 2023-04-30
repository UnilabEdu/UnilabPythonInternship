from flask import Flask, render_template, url_for, flash, redirect, session
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired, length, Email, InputRequired
from wtforms.widgets import TextArea
from werkzeug.utils import secure_filename
app = Flask(__name__)

app.config['SECRET_KEY'] = 'ITISHUGESECRET'

serverPort = 8085

pages = (
    ("home", "Home"),
    ("book", "Book now"),
    ("rooms", "Rooms"),
    ("contact", "Contact us"),
)

table_headers = ["#", "Room Type", "Price", "Quantity"]

table_rows = (
    (1, "Double", "80$", 20),
    (2, "Triple", "110$", 5),
    (3, "Quadruple", "130$", 5),
    (4, "Family", "150$", 4)
)

table = {
    "headers": table_headers,
    "rows": table_rows
}




class FormName(FlaskForm):
    name = StringField('First Name',
                       validators=[
                           DataRequired(),
                           length(min=2, max=35)
                       ],
                       render_kw={"placeholder":"E.g John"}
                       )
    lastname = StringField('Last Name',
                           validators=[
                               DataRequired(),
                               length(min=2, max=35)
                           ],
                           render_kw={"placeholder": "E.g Smith"}
                           )
    email = StringField('Enter your E-mail',
                        validators=[
                            InputRequired(),
                            length(max=35),
                            Email(message="Wrong format!")
                        ],
                        render_kw={"pLaceholder": "example@example.com"}
                        )
    message = StringField('Leave your message here!', validators=[DataRequired()], widget=TextArea())
    submit = SubmitField('Submit')

class FormBook(FlaskForm):
    name = StringField('First Name',
                       validators=[
                           DataRequired(),
                           length(min=2, max=35)
                       ],
                       render_kw={"placeholder":"E.g John"}
                       )
    lastname = StringField('Last Name',
                           validators=[
                               DataRequired(),
                               length(min=2, max=35)
                           ],
                           render_kw={"placeholder": "E.g Smith"}
                           )
    date_from = DateField('From')
    date_to = DateField('To')
    select_adult = SelectField('Number of adults', choices=[("1"),("2"),("3"),("4"),("5")])
    select_child = SelectField('Number of children (under 6 years)', choices=[("1"), ("2"), ("3"), ("4"), ("5")])
    title = StringField("Name of your file")
    file = FileField(validators=[FileRequired()])
    submit = SubmitField('Submit reservation')


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", pages=pages)


@app.route("/book", methods=['GET', 'POST'])
def book():

    name = None
    lastname = None
    date_from = None
    date_to = None
    select_adult = None
    select_child = None
    form = FormBook()

    if form.validate_on_submit():
        if form.title.data:
            file_name = secure_filename(form.title.data)
        else:
            file_name = secure_filename(form.file.data.filename)
        form.file.data.save(f"static/{file_name}")
        session['name'] = form.name.data
        session['lastname'] = form.lastname.data
        session['date_from'] = form.date_from.data
        session['date_to'] = form.date_to.data
        session['select_adult'] = form.select_adult.data
        session['select_child'] = form.select_child.data

        return redirect(url_for("thank_you"))

    return render_template("book_now.html", pages=pages, form=form, name=name, lastname=lastname, date_from=date_from, date_to=date_to,
                           select_adult=select_adult, select_child=select_child)


@app.route("/thank_you")
def thank_you():
    return render_template("thankyou.html")


@app.route("/rooms")
def rooms():
    return render_template("room_info.html", pages=pages, table=table)


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    name = None
    lastname = None
    email = None
    form = FormName()

    if form.validate_on_submit():
        name = form.name.data
        lastname = form.lastname.data
        email = form.email.data
        flash(f"Thank you {name} {lastname} you have successfully sent us a message, we will reach you back on {email}")
        form.name.data = ''
        form.lastname.data = ''
        form.email.data = ''
        return redirect(url_for("contact"))

    return render_template("contact_us.html", pages=pages, form=form, name=name, lastname=lastname, email=email)


if __name__ == "__main__":
    app.run(port=serverPort, debug=True)
