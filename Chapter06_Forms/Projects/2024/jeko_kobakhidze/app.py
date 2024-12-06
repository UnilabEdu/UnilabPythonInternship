from flask import Flask, render_template, redirect, url_for, flash
from forms import RegistrationForm, SurveyForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '1rm32fm3f3f'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)

@app.route('/survey', methods=['GET', 'POST'])
def survey():
    form = SurveyForm()
    if form.validate_on_submit():
        flash('Survey submitted successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('survey.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
