# Database In Views

ამ თავში ვნახავთ როგორ შეგვიძლია მონაცემთა ბაზა დავუკავშიროთ ვებ ინტერფეისს.

## შესავალი

ამ დროისთვის უკვე გავეცანი იმ ძირითად კომპონენტებს რაც ვებ გვერდის აწყობისთვის დაგვჭირდება. ვნახეთ თუ როგორ უნდა:

- გამოვიტანოთ შაბლონები და განვალაგოთ მათში დინამიური ინფორმაცია
- მივიღოთ მომხმარებლისგან მონაცემი ფორმების დახმარებით
- შევინახოთ ინფორმაციები მონაცემთა ბაზაში და მოვარგოთ მას API
- უკან ამოვიღოთ მონაცემთა ბაზიდან ინფორმაცია

view ეწოდება სივრცეს რომელზეც გვერდის შიგთავსი და ფუნქციონალური ელემენტებია განლაგებული. ჩვენ ვნახავთ როგორ ავაწყოთ სხვადასხვა გვერდის view მომხმარებლისთვის, აქამდე მიღებული გამოცდილებით.

## შესავალი

პირველ რიგში შევქმნათ ორი ფაილი: `portal.py` და `forms.py`

ასევე დაგვჭირდება `templates` დირექტორია, პროექტის შაბლონების განსათავსებლად.

პირველრიგში templates დირექტორიაში მოვათავსებთ `base.html` -ს და `home.html` -ს.

იგივე დირექტიროიაში დავამატოთ 3 view, შესაბამისი დანიშნულებისთვის:

1. add.html - სტუდენტის დასამატებლად
2. delete.html - სტუდენტის წასაშლელად
3. list.html - სტუდენტების გამოსატანად

ეს არის საბაზისო სტრუქტურა რომლის სქილინგი პროექტის სირთულის შესაბამისად არის შესაძლებელი.

## კოდი

### portal.py

პირველ რიგში ავაწყოთ პორტალის საიტის პითონის კოდი. ამისთვის შემოვიტანოთ საჭირო ბიბლიოთეკები და გავწეროთ კონფიგურაცია:

```python
import os
from forms import  AddForm , DelForm # მოგვიანებით ამ ფორმებს შევქმნით და შემოვიტანთ forms.py-დან
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)
# Key for Forms
app.config['SECRET_KEY'] = 'mysecretkey'

############################################

        # SQL DATABASE კონფიგურაცია

##########################################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

if __name__ == '__main__':
    app.run(debug=True)
```

ავაწყოთ სტუდენტისთვის მონაცემთა ბაზის მოდელი:

```python
class Student(db.Model):

    __tablename__ = 'students'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return f"Student name: {self.name}"
```

დადგა დრო ვიუ ფუნქციების აწყობის. მათი დახმარებით შევძლებთ მოთხოვნის შესაბამისი კონტენტის გამოტანას მომხმარებლეთან. მათში ასევე მოვათავსებთ ფორმებს, რომლიდან აღებულ ინფორმაციასაც დავაკავშირებთ მონაცემთა ბაზასთან:

```python
@app.route('/')
def index():
    return render_template('about.html')
```

გავაკეთოთ ბმული მონაცემის დასამატებელ ფორმასთან. ამისთვის წინასწარ დაგვჭირდება ფორმის გამზადება [`forms.py` ფაილში](#forms.py).

```python
@app.route('/add', methods=['GET', 'POST'])
def add_stu():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data

        # Add new Student to database
        new_stu = Student(name)
        db.session.add(new_stu)
        db.session.commit()

        return redirect(url_for('list_stu'))

    return render_template('add.html',form=form)
```

როგორც კოდიდან ხედავთ, მონაცემის დამატების შემდგომ ხდება მომხმარებლის გადამისამართება ბმულზე რომელსაც ბაზაში არსებული მონაცემების სია გამოაქვს. ავაწყოთ ეს ბმული შესაბამისი ფუნქციონალით:

```python
@app.route('/list')
def list_stu():
    # Grab a list of Students from database.
    students = Student.query.all()
    return render_template('list.html', students=students)
```

საბოლოოდ კი დავამატოთ ბმული ფუნქციონალზე რომელიც მონაცემს წაგვიშლის ბაზიდან:

```python
@app.route('/delete', methods=['GET', 'POST'])
def del_stu():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        stu = Student.query.get(id)
        db.session.delete(stu)
        db.session.commit()

        return redirect(url_for('list_stu'))
    return render_template('delete.html',form=form)
```

### forms.py

შემოვიტანოთ სამუშაო ბიბლიოთეკები და ფორმის ასაწყობად საჭირო ელემენტები, ამოსაღები ინფორმაციის გათვალისწინებით:

```python
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
```

ავაწყოთ მონაცემის ჩაწერის ფორმა:

```python
class AddForm(FlaskForm):

    name = StringField('Name of Student:')
    submit = SubmitField('Add Student')
```

და მონაცემის ამოშლის ფორმა:

```python
class DelForm(FlaskForm):

    id = IntegerField('Id Number of Student to Remove:')
    submit = SubmitField('Remove Student')
```

### base.py

გავუკეთოთ გვერდის საბაზისო თემფლეითს ნავიგაციის პანელი, რომელიც მომხმარებელს მისცემს შესაძლებლობას გვერდებს შორის გადაადგილების. ასევე გამოვყოთ სივრცე გვერდის კონტენტის ჩასატვირთად ბლოკ ელემენტის დახმარებით:

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8" />
    <link
      rel="stylesheet"
      href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
      integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
      crossorigin="anonymous"
    />
    <script
      src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
      integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
      integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
      integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
      crossorigin="anonymous"
    ></script>

    <title>Students Portal</title>
  </head>
  <body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="navbar-nav">
        <a class="nav-item nav-link" href="{{ url_for('index') }}">Home</a>
        <a class="nav-item nav-link" href="{{ url_for('add_stu') }}"
          >Add Student</a
        >
        <a class="nav-item nav-link" href="{{ url_for('list_stu') }}"
          >List of Students</a
        >
        <a class="nav-item nav-link" href="{{ url_for('del_stu') }}"
          >Delete Student</a
        >
      </div>
    </nav>

    {% block content %} {% endblock %}
  </body>
</html>
```

### home.html

```jinja
{% extends "base.html" %}
{% block content %}
<div class="jumbotron">
  <h1>Welcome to our Student Portal</h1>
  <p>Please select one of the links from the nav bar.</p>
</div>
{% endblock %}
```

### list.html

```jinja
{% extends "base.html" %}
{% block content %}
<div class="jumbotron">
  <h1>Here is a list of all available Students.</h1>
  <ul>
    {% for student in students  %}
    <li>{{student}}</li>
    {% endfor %}
  </ul>

</div>
{% endblock %}
```

### add.html

```jinja
{% extends "base.html" %}
{% block content %}
<div class="jumbotron">
  <h1>Are you a new student?</h1>
  <p>Add a new student with the form below:</p>
  <form method="POST">
      {# This hidden_tag is a CSRF security feature. #}
      {{ form.hidden_tag() }}
      {{ form.name.label }} {{ form.name() }}
      {{ form.submit() }}
  </form>
</div>
{% endblock %}
```

### delete.html

```jinja
{% extends "base.html" %}
{% block content %}
<div class="jumbotron">
  <h1>Did a student graduate?</h1>
  <p>Fill out the form to remove the student from the list.</p>
  <form method="POST">
      {# This hidden_tag is a CSRF security feature. #}
      {{ form.hidden_tag() }}
      {{ form.id.label }} {{ form.id() }}
      {{ form.submit() }}
  </form>
</div>
{% endblock %}
```
