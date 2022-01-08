from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, SubmitField
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['SECRET_KEY'] = "mySECRETkey"


class PhotoForm(FlaskForm):
    title = StringField("ფაილის დასახელება")
    file = FileField(validators=[FileRequired()])
    submit = SubmitField("ატვირთვა")


@app.route('/', methods=['GET', 'POST'])
def upload():
    form = PhotoForm()
    if form.validate_on_submit():
        if form.title.data:
            file_name = secure_filename(form.title.data)
        else:
            file_name = secure_filename(form.file.data.filename)
        print(f"ვინახავ ფაილს სახელწოდებით {file_name}")
        form.file.data.save(f'uploads/{file_name}')
        return redirect(url_for('upload'))
    return render_template('upload.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
