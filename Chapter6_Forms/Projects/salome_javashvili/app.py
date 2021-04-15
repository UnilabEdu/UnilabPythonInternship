from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, length, EqualTo, AnyOf
import data
from flask_bootstrap import Bootstrap
from country_list import countries_for_language

app = Flask(__name__)

app.config['SECRET_KEY'] = "mySeCrEtKey"

Bootstrap(app)


class SearchForm(FlaskForm):
    type = SelectField('Pathogen Type',
                       choices=[(i, i) for i in data.pathogens]
                       )
    genus = StringField('Genus')
    species = StringField('Species')
    strain = StringField('Strain')
    region = SelectField('Region',
                         choices=[(i, i) for i in data.regions])
    start = SelectField('From:',
                        choices=[(i, i) for i in range(2000, 2022)])
    end = SelectField('To:',
                      choices=[(i, i) for i in range(2000, 2022)])
    check = BooleanField('Search for a genotype')
    fasta = TextAreaField('Genotype (FASTA format):')
    submit = SubmitField('Search')


@app.route('/home', methods=['GET', 'POST'])
def home():
    form = SearchForm()
    check = form.check.data
    title1 = "Database for Pathogen Prevalence"
    title2 = "In Georgia"
    title3 = "Pathogen Search"
    if form.validate_on_submit():
        type = form.type.data
        genus = form.genus.data
        species = form.species.data
        strain = form.strain.data
        region = form.region.data
        start = form.start.data
        end = form.end.data
        fasta = form.fasta.data
    return render_template("home.html", pathogens=data.pathogens, form=form,
                           titles=[title1, title2, title3], base='base.html')


class SearchFormGE(FlaskForm):
    type = SelectField('პათოგენის ტიპი',
                       choices=[(i, i) for i in data.pathogens_ge]
                       )
    genus = StringField('გვარი')
    species = StringField('სახეობა')
    strain = StringField('შტამი')
    region = SelectField('რეგიონი',
                         choices=[(i, i) for i in data.regions_ge])
    start = SelectField('როდიდან:',
                        choices=[(i, i) for i in range(2000, 2022)])
    end = SelectField('როდემდე:',
                      choices=[(i, i) for i in range(2000, 2022)])
    check = BooleanField('გენოტიპის მოძებნა')
    fasta = TextAreaField('გენოტიპი (FASTA ფორმატით):')
    submit = SubmitField('ძებნა')


@app.route('/home_ge', methods=['GET', 'POST'])
def home_ge():
    form = SearchFormGE()
    check = form.check.data
    title1 = "საქართველოში გავრცელებულ პათოგენთა"
    title2 = "მონაცემთა ბაზა"
    title3 = "პათოგენთა სარჩევი"
    if form.validate_on_submit():
        type = form.type.data
        genus = form.genus.data
        species = form.species.data
        strain = form.strain.data
        region = form.region.data
        start = form.start.data
        end = form.end.data
        fasta = form.fasta.data
    return render_template("home.html", pathogens=data.pathogens_ge, form=form, check=check,
                           titles=[title1, title2, title3], base='base_ge.html')


class LoginForm(FlaskForm):
    email = StringField("", [DataRequired(), Email()])
    password = StringField("", [DataRequired()])
    submit = SubmitField("Log In")


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        session['email'] = form.email.data
        session['password'] = form.password.data
        return redirect(url_for('home'))
    return render_template("login.html", form=form)


class LoginFormGE(FlaskForm):
    email = StringField("", [DataRequired(), Email()])
    password = StringField("", [DataRequired()])
    submit = SubmitField("შესვლა")


@app.route('/login_ge', methods=['GET', 'POST'])
def login_ge():
    form = LoginFormGE()

    if form.validate_on_submit():
        session['email'] = form.email.data
        session['password'] = form.password.data
        return redirect(url_for('home_ge'))
    return render_template("login_ge.html", form=form)


countries = dict(countries_for_language('en'))
required_message = 'Please fill in the form'


class SignupForm(FlaskForm):
    name = StringField("First Name", [DataRequired(message=required_message)])
    surname = StringField("Last Name", [DataRequired(message=required_message)])
    city = StringField("City", [DataRequired(message=required_message)])
    country = StringField("Country",
                          [DataRequired(message=required_message),
                           AnyOf(countries.values(), message='Select a valid country')])
    company = StringField("Company / Institution", [DataRequired(message=required_message),
                                                    length(min=3, message='Min. 3 symbols')])
    position = StringField("Position", [DataRequired(message=required_message),
                                        length(min=3, message='Min. 3 symbols')])
    email = StringField("Company / Institution Email", [DataRequired(message=required_message),
                                                        Email()])
    password = StringField("Password", [DataRequired(message=required_message),
                                        length(min=8, message='Min. 8 symbols'),
                                        EqualTo('re_password', message='Passwords do not match')])
    re_password = StringField("Repeat Password", [DataRequired(message=required_message)])
    acceptance = BooleanField('Agree to terms and conditions', [DataRequired(message=required_message)])
    submit = SubmitField("Sign Up")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    title = "Sign Up"
    if form.validate_on_submit():
        name = form.name.data
        surname = form.surname.data
        city = form.city.data
        country = form.country.data
        company = form.company.data
        position = form.position.data
        email = form.email.data
        password = form.password.data
        re_password = form.re_password.data
        acceptance = form.acceptance.data
        flash('You signed up successfully')
        print(name, surname, city, country, company, position, email, password, re_password, acceptance)
        return redirect(url_for('signup'))
    return render_template("signup.html", form=form, title=title, base='base.html')


required_message_ge = 'გთხოვთ, შეავსოთ ფორმა'


class SignupFormGE(FlaskForm):
    name = StringField("სახელი", [DataRequired(message=required_message_ge)])
    surname = StringField("გვარი", [DataRequired(message=required_message_ge)])
    city = StringField("ქალაქი", [DataRequired(message=required_message_ge)])
    country = StringField("ქვეყანა", [DataRequired(message=required_message_ge)])
    company = StringField("კომპანია/ დაწესებულება", [DataRequired(message=required_message_ge),
                                                     length(min=3, message='უნდა შეიცავდეს მინიმუმ 3 სიმბოლოს')])
    position = StringField("თანამდებობა", [DataRequired(message=required_message_ge),
                                           length(min=3, message='უნდა შეიცავდეს მინიმუმ 3 სიმბოლოს')])
    email = StringField("ოფიციალური მეილი", [DataRequired(message=required_message_ge),
                                             Email(message='გთხოვთ, ჩაწეროთ იმეილი')])
    password = StringField("პაროლი", [DataRequired(message=required_message_ge),
                                      length(min=8, message='პაროლი უნდა შეიცავდეს მინიმუმ 8 სიმბოლოს'),
                                      EqualTo('re_password', message='პაროლები ერთმანეთს არ ემთხვევა')])
    re_password = StringField("გაიმეორეთ პაროლი:", [DataRequired(message=required_message_ge)])
    acceptance = BooleanField('ვეთანხმები წესებს და პირობებს',
                              [DataRequired(message='დასარეგისტრირებლად უნდა დაეთანხმოთ წესებს და პირობებს')])
    submit = SubmitField("დარეგისტრირება")


@app.route('/signup_ge', methods=['GET', 'POST'])
def signup_ge():
    form = SignupFormGE()
    title = "რეგისტრაცია"

    if form.validate_on_submit():
        name = form.name.data
        surname = form.surname.data
        city = form.city.data
        country = form.country.data
        company = form.company.data
        position = form.position.data
        email = form.email.data
        password = form.password.data
        re_password = form.re_password.data
        acceptance = form.acceptance.data
        flash('თქვენ წარმატებით დარეგისტრირდით')
        print(name, surname, city, country, company, position, email, password, re_password, acceptance)
        return redirect(url_for('signup_ge'))
    return render_template("signup.html", form=form, title=title, base='base_ge.html')


if __name__ == '__main__':
    app.run(debug=True)
