from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


class SimpleForm(FlaskForm):
    submit = SubmitField('დააჭირე აქ')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SimpleForm()

    if form.validate_on_submit():
        flash("თქვენ წარმატებით დააჭირეთ ღილაკს")
        return redirect(url_for('index'))

    return render_template('home.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
