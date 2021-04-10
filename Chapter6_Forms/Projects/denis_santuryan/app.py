from flask import Flask, render_template, url_for, session, redirect, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired, length, EqualTo, Email

app = Flask(__name__)

app.config['SECRET_KEY'] = "SecretKey00"

pages_nav_list = (
    ("index", "მთავარი"),
    ("about", "ჩვენს შესახებ"),
    ("contact", "კონტაქტი"),
    ("auth", "შესვლა"),
)


class SignInForm(FlaskForm):
    email = StringField('შეიყვანეთ მეილი: ',
                        validators=[
                            DataRequired(message="მეილის შეყვანა აუცილებელია"),
                            length(min=8, max=100, message="არასწორადაა შეყვანილი"),
                            Email(message="არაა შეყვანილი მეილი")
                        ])
    password = StringField('შეიყვანეთ პაროლი: ',
                           validators=[
                               DataRequired(),
                               length(min=6, max=18),
                           ])
    submit = SubmitField('შესვლა')


class RegisterForm(FlaskForm):
    name_first = StringField('შეიყვანეთ სახელი: ',
                             validators=[
                                 DataRequired(message="სახელის შეყვანა აუცილებელია")
                             ])
    name_last = StringField('შეიყვანეთ გვარი: ',
                            validators=[
                                DataRequired(message="გვარის შეყვანა აუცილებელია")
                            ])
    sex = RadioField('აირჩიეთ სქესი: ',
                     choices=[
                         ('0', 'მდედრობითი'),
                         ('1', 'მამრობითი'),
                         ('2', 'სხვა')
                     ])
    mail = StringField('შეიყვანეთ მეილი: ',
                       validators=[
                           DataRequired(message="მეილის შეყვანა აუცილებელია"),
                           length(min=8, max=100, message="არასწორადაა შეყვანილი"),
                           Email(message="არაა შეყვანილი მეილი")
                       ])
    phone = StringField('შეიყვანეთ მობ. ნომერი: ',
                        validators=[DataRequired(message="ნომრის შეყვანა აუცილებელია"),
                                    length(min=9, max=18, message="არასწორადაა შეყვანილი")
                                    ])
    passw = StringField('შექმენით პაროლი: ',
                        validators=[
                            EqualTo("conf_pass", message="პაროლები არ ემთხვევა"),
                            DataRequired(message="პაროლის შეყვანა აუცილებელია"),
                            length(min=8, max=18, message="პაროლი უნდა შედგებოდეს 8-18 სიმბოლოსგან")
                        ])
    conf_pass = StringField('გაიმეორეთ პაროლი: ')
    submit = SubmitField('რეგისტრაცია')


@app.route('/home')
def index():
    return render_template('placeholder.html', pages=pages_nav_list)


@app.route('/about')
def about():
    return render_template('placeholder.html', pages=pages_nav_list)


@app.route('/contact')
def contact():
    return render_template('placeholder.html', pages=pages_nav_list)


@app.route('/', methods=['GET', 'POST'])
def auth():
    form_sign_in = SignInForm()
    form_register = RegisterForm()
    if request.method == 'POST':
        if form_sign_in.validate_on_submit():
            session['email'] = form_sign_in.email.data
            session['password'] = form_sign_in.password.data
            flash('წარმატებით შეხვედით სისტემაში!')
            return redirect(url_for('success_auth'))

        elif form_register.validate_on_submit():
            session['name_first'] = form_register.name_first.data
            session['name_last'] = form_register.name_last.data
            session['sex'] = form_register.sex.data
            session['mail'] = form_register.mail.data
            session['phone'] = form_register.phone.data
            session['passw'] = form_register.passw.data
            session['conf_pass'] = form_register.conf_pass.data
            flash('რეგისტრაცია წარმატებით დასრულდა!')
            return redirect(url_for('success_register'))
        else:
            flash('მონაცემები არასწორადაა შეყვანილი. თავიდან სცადეთ. ')
    return render_template('auth.html', pages=pages_nav_list, form_sign_in=form_sign_in, form_register=form_register)


@app.route('/success_auth')
def success_auth():
    return render_template('success_auth.html', pages=pages_nav_list)


@app.route('/success_register')
def success_register():
    return render_template('success_register.html', pages=pages_nav_list)


if __name__ == '__main__':
    app.run(port=5080, debug=True)
