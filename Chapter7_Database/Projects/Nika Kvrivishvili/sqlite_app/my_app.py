from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import sqlite3

app = Flask(__name__)

app.config['SECRET_KEY'] = "nika var"


class ForName(FlaskForm):
    name = StringField("name: ", [DataRequired()])
    age = StringField("age: ", [DataRequired()])
    submit = SubmitField('add')


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    age = None
    form = ForName()

    conn = sqlite3.connect('profiles.db')
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS students (name TEXT, age INTEGER)")
    data = cursor.execute("SELECT * FROM students").fetchall()

    conn.commit()
    conn.close()

    if form.validate_on_submit():
        name = form.name.data
        age = form.age.data

        profile_info = [(name, age)]

        conn = sqlite3.connect('profiles.db')
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS students (name TEXT, age INTEGER)")

        cursor.executemany("INSERT INTO students VALUES (?,?) ", profile_info)

        data = cursor.execute("SELECT * FROM students").fetchall()

        conn.commit()
        conn.close()

        form.name.data = ''
        form.age.data = ''
        redirect(url_for('index'))

    # shekithva form name age
    return render_template('index.html', form=form, data=data)


if __name__ == "__main__":
    app.run(debug=True)
