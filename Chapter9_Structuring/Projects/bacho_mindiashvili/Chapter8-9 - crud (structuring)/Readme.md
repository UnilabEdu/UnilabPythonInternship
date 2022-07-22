# სტრუქტურიზაცია

წინა რამოდენიმე თავში უკვე შევხვდით ერთ ფაილში დიდი ზომის კოდის დაგროვების პრობლემას, რაც სამუშაო პროცესს და კოდის აღქმის პროცესს ართულებს. რაც უფრო იზრდება პროექტი ზომაში, მით უფრო ხშირად იჩენს ეს პრობლემა თავს. შესაბამისად, სასურველია პროექტის დაწყებიდან ვიფიქროთ პროგრამის პრაქტიკულ სტრუქტურიზაციასა და კოდის ოპტიმიზაციაზე. წინა თავებში გავეცანით რამოდენიმე მეთოდს, დღეს კი ამ ყველაფერს დავამატებთ flask აპლიკაციის სტრუქტურიზაციის ერთ-ერთ ფორმას (დაფუძნებულია flask-ის მიერ შემოთავაზებულ პროექტის სტრუქტურაზე) და გავერთიანებთ ამ ცოდნას ერთ პროექტში.

## შესავალი

წინა თავში ძალიან ბევრი რამ მოგვიგროვდა ძირითად `app`/`portal.py`-ში. მიუხედავად იმისა რომ ფორმების გენერატორი ცალკე `form.py` ფაილში გავიტანეთ, რაც სტრუქტურიზაციის ძალიან კარგი პრაქტიკაა, მთავარ ფაილში კიდევ ბევრი რამ დაგვრჩა დასანაწილებელი.

როგორც შევთანხმდით, `app.py` -ში უნდა მოთავსდეს სერვერული აპლიკაციის გასაშვებად საჭირო კოდი, ბიბლიოთეკები, კონფიგურაცია, რესურსებთან ბმა. კოდის სხვა დანარჩენი ნაწილი უნდა მოვათავსოთ ოპტიმალურ ფაილებში და გავუკეთოთ ბმა ცენტრალურ `app.py` -სთან. ამისთვის აუცილებელია პროგრამა დავყოთ ფუნქციონალურ პორციებად და განავათავსოთ შესაბამის ფაილებში.
მაგალითად:

- მოდელები => `models.py`
- გვერდი view -ები => `views.py`

## შაბლონი

სტრუქტურიზაციის პროცესი გვეხმარება დეველოპმენტ პროცესის კომფორტულად წამართვაში. აუცილებელია პროექტს გავუკეთოთ ისეთი სტრუქტურა, რომ როგორც ერთი დეველოპერის ისე დეველოპერთა გუნდისთვისაც მარტივი აღსაქმელი და მისახვედრი იყოს, სად რა არის მოთავსებული.

ამისთვის პროექტი უნდა დავყოთ შემადგენელ ძირითად ელემენტებად და ამ ელემენტების სამუშაოდ საჭირო კომპონენტებად (რომელიც თავის თავში შეიძლება მოიცავდეს ქვერესურსებს). შესაბამისად ვიღებთ ხისებრ სტრუქტურას სადაც ყველაფერი უკავშირდება ძირითად სერვერულ აპლიკაციას.

მაგალითისთვის განვიხილოთ წინა თავისთვის შერჩეული პროექტი და ვეცადოთ მის სტრუქტურიზებას შაბლონის მიხედვით. გაითვალისწინეთ რომ ეს არ არის მკაცრად განსაზღვრული წესი თუ როგორი სტრუქტურა უნდა ჰქონდეს თქვენს პროექტს, არამედ უფრო შემოთავაზება თუ როგორ მოაწყოთ ოპტიმალური გარემო.

შესაბამისად წინა თავში განხილული სტუდენტ-მასწავლებლის პროექტის სტრუქტურიზაცია ასეა შესაძლებელი:

```tre
📦StudentPortal
├───app.py # მთავარი app.py რომლის გამოძახებითაც გაეშვება web app სერვერი
├───requirements.txt # პროექტისთვის საჭირო ბიბლიოთეკების სია pip install-თ დასაყენებლად
├───📂migrations # ფოლდერი შექმნილი მიგრაციებისთვის
├───📂myproject # პროექტის რესურსების მთავარი ფოლდერები, კომპონენტები გადანაწილებულია სუბ-ფოლდერებში
│   │  __init__.py   # აპლიკაციის აღწერა და კონფიგურაცია
│   │
│   ├───📂static # ადგილი სტატიკური ფაილებისთვის: CSS, JS, Images, Fonts, etc...
│   ├───📂templates # ვებ აპლიკაციის ძირითადი/სასტარტო შაბლონები
│   │   │    base.html
│   │   │    home.html
│   │  				# კომპონენტების საზიარო რესურსები
│   │  data.sqlite # ლოკალური ბაზა
│   │  models.py # ბაზის მოდელები
│   │  				# კომპონენტები
│   ├───📂teachers
│   │   │   forms.py
│   │   │   views.py
│   │   │
│   │   ├───📂templates
│   │   │   └───📂teachers
│   │   │       │   add_teachers.html
... ...
... ...
│   ├───📂students
│   │   │   forms.py
│   │   │   views.py
│   │   │
│   │   ├───📂templates
│   │   │   └───📂students
│   │   │       │   add.html
│   │   │       │   delete.html
│   │   │       │   list.html
```

რაც უფრო იზრდება პროექტი მით უფრო იზრდება აპლიკაციის სამუშაო კოდის ზომა. როგორც ხედავთ გარდა იმისა, რომ გავმიჯნეთ ერთმანეთისგან სერვერის დასასტარტად და პროექტის სამუშაოდ საჭირო რესურსები, მოვათავსეთ ეს რესურსები საერთო `myproject` დირექტორიაში. შემდგომ ამ დირექტორიაში რესურსებს გავუკეთეთ ცალკე კატეგორიზაცია, მაგალითად ცალკე მოვათავსეთ შაბლონები, ცალკე ბაზის მოდელები და ქვე დირექტორიებად გავიტანეთ სამუშაო ობიექტები - კომპონენტები.

პრაქტიკულია თუ პროექტს ასე დავყოფთ შემადგენელ კომპონენტებად - იმ ობიექტებად, რომლის გარშემოც შესაძლებელია რესურსების დაჯგუფება და სტრუქტურიზაცია.

ჩვენი შემთხვევისთვის გვაქვს მსგავსი ორი კომპონენტი: students - მოსწავლეები და teachers - მასწავლებლები. მათ გააჩნიათ ქვეკომპონენტები: ფორმები და ვიუები და ქვერესურსები - შაბლონები.

## გადანაწილება

მას შემდეგ რაც თეორიულად მიმოვიხილეთ თუ როგორი სტრუქტურა უნდა ჰქონდეს პროექტს, გადავანაწილოთ და დავსვათ წინა თავში აწყობილი პროექტი შესაბამის სტრუქტურაზე. ამისთვის ძირითადად ახალი დირექტორიების შექმნა და მათში წინა თავიდან `copy` / `paste` გადმოტანილი ფაილების ოპტიმიზაცია დაგვჭირდება. (რადგან კოდის ძირითადი ნაწილი უკვე დავწერეთ წინა თავში).

პროცესის გამარტივებაში დაგვეხმარება flask-ში ჩაშენებული blueprints შესაძლებლობები, რომლითაც გავწერთ მოდულარ კომპნენტებს, მაგალითად დავაკავშირებთ მათ შესაბამის ვიუებთან.

მაგალითისთვის, ჩვენ გვექნება ორი `views.py` ფაილი, ერთი მასწავლებლების კომპონენტისთვის ხოლო მეორე სტუდენტების. თითოეულ ამ ფაილს ექნება თავისი `add view`. იმისთვის რომ დავეხმაროთ flask -ს განასხვავოს `/add` მარშუტები, ჩვენ გამოვიყენებთ ბლუპრინტს.

ბლუპრინტის მეშვეობით გავწერთ მისამართის პრეფიქსებს თითოეული view ფაილისთვის. მაგალითად:

> `/students/add`
>
> `/teachers/add`

შესაბამისად დღევანდელი ჩვენი სამუშაოა:

- არსებული კოდის რესტრუქტურიზაცია და შესაბამის ფოლდერებში დაბინავება
- პროექტის ახალი სტრუქტურის შესაბამისად კოდის გამართვა
- პროექტში ბლუპრინტის ჩამატება
- ბლუპრინტის გაწერა `__init__.py` ფაილში.

შაბლონის მიხედვით შევქმნათ ფოლდერები და ფაილები. შემდეგ ქვეთავში ვნახავთ როგორ უნდა გავმართოთ კოდი ამ სტრუქტურის მიხედვით:

### კოდის გამართვა

ინდივიდუალურად გაგიზიარებთ თითოული ფაილის შიგთავს კოდს თქვენ კი მოარგეთ კოდები თქვენს პროექტს.

### app.py

```python
from myproject import app
from flask import render_template

@app.route('/')
def index():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)

```

### /myproject

#### `models.py`

იმის გათვალისწინებით რომ სულ ორი მოდელი გვაქვს პროექტში, მისაღებია მათი ერთ ფაილში დატოვება, რადგან კოდის ზედმეტად დანაწევრებაც არ არის საჭირო. თუმცა თუ თქვენი მოდელების ზომა და მათში შემავალი მეთოდები დიდია რა საკვირველია სასურველია მათი სტრუქტურიზაციაც.

```python
from myproject import db


class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    #  One_to_one relationship
    # A student only has one teacher, thus uselist is False.
    # Strong assumption of 1 teacher per 1 student and vice versa.
    teacher = db.relationship('Teacher', backref="student", uselist=False)

    def __init__(self, name):
        # მხოლოდ გვჭირდება ამ ბაზის მოდელისთვის უნიკალური წევრის ატრიბუტის აღწერა
        self.name = name

    def __repr__(self):
        if self.teacher:
            return f"Teacher of the Student {self.name} is {self.teacher.name}"
        else:
            return f"Student {self.name} has no teacher yet"


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Connect the teacher to the Student that "owns" it.
    # We use student.id because __tablename__='student'
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    name = db.Column(db.String)

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def __repr__(self):
        return f"Teacher Name: {self.name}"
```

ერთადერთი განსხვავება რაც ძველი კოდისგან გვაქვს არის `from myproject import db` ეს იმიტომ რომ ჩვენ სერვერული პროგრამის აღწერას (შესაბამისად ფლასკის კონფიგურაციის და მონაცემთა ბასიზაც) გადავიტანთ `myproject/__init__.py` -ფაილში.

#### `__init__.py`

```python
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

# თუ კონფიგურაციისათვის იყენებთ ბევრ პარამეტრს სასურველია მათი config.py ფაილში გადანაწილება
app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

# გაითვალისწინე! აუცილებელია იმპორტების გაკეთება მას შემდეგ რაც db ობიექტს გაწერ
# წინააღმდეგ შემთხვევაში models.py დაგვიერორდება.
## ბაზასთან მომუშავე views.py ფაილები სათითაოდ შემოვიტანოთ მათი ბლუპრინტებით
from myproject.students.views import students_blueprint
from myproject.teachers.views import teachers_blueprint

# ამის შემდგომ უკვე შეგვიძლია ბლუპრინტების რეგისტრირება
app.register_blueprint(students_blueprint,url_prefix="/students")
app.register_blueprint(teachers_blueprint,url_prefix='/teachers')

```

ბლუპრინტებმა არ დაგაბნიოთ ამ ეტაპზე. როდესაც `views` გავწერთ იქ ვისაუბრებთ თუ რას აკეთებენ ამ ეტაპისთვის უხილავ ნაწილში.

ისევე როგორც API -ს ვამატებდით წინასწარ გაწერილ ობიექტს. აქაც მსგავსი სტრუქტურა გვაქვს. პროექტში შემოგვაქვს ვიუები რომელიც მოთავსებულია შესაბამისი ვიუს ბლუპრინტში (მაგ. `students_blueprint`) და `register_blueprint()` მეთოდის გამოყენებით, ჩვენს აპლიკაციაში ვარეგისტრირებთ ვიუ რესურსს შესაბამის მისამართზე.

და როგორც API-ს შემთხვევაში, ნებისმიერი ფუნქციონალი რომელიც რესურსში იყო გაწერილი ავტომატურად აქტიურდებოდა შესაბამის მისამართსა თუ მეთოდის ტიპზე, ანალოგიურად გააქტიურდება ვიუში გაწერილი ფუნქციონალები, ბლუპრინტის მიხედვით.

### /templates

#### `base.html`

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>სტუდენტის პორტალი</title>
    <!-- CSS only -->
    <link
      rel="stylesheet"
      href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
      integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z"
      crossorigin="anonymous"
    />

    <!-- JS, Popper.js, and jQuery -->
    <script
      src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
      integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"
      integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"
      integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV"
      crossorigin="anonymous"
    ></script>
  </head>
  <body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="navbar-nav">
        <a class="nav-item nav-link" href="{{ url_for('home') }}">თავფურცელი</a>
        <a class="nav-item nav-link" href="{{ url_for('student.add') }}"
          >სტუდენტის დამატება</a
        >
        <a class="nav-item nav-link" href="{{ url_for('student.list') }}"
          >სტუდენტის სია</a
        >
        <a class="nav-item nav-link" href="{{ url_for('student.delete') }}"
          >სტუდენტის წაშლა</a
        >
        <a class="nav-item nav-link" href="{{ url_for('teacher.add') }}"
          >მასწავლებლის დამატება</a
        >
      </div>
    </nav>

    {% block content %} {% endblock %}
  </body>
</html>
```

#### `home.html`

```jinja2
{% extends "base.html" %}
{% block content %}
    <div class="jumbotron">
        <h1>მოგესალმებით სტუდენტის პლატფორმაზე</h1>
        <p>გთხოვთ აირჩიოთ შესაბიმისი ფუნქციონალი სანავიგაციო ველიდან</p>
    </div>
{% endblock %}

```

როგორც ხედავთ home.html წინა თავის იდენტურია. აქ შეგიძლიათ ნებისმიერი კონტენტი მოათავსოთ რისი გამოჩენაც ამ თემფლეითის ჩატვირთვისას გსურთ.

## components

### myproject/<component>/forms.py

ორივე კომპონენტის ფორმების ფაილს ერთ ქვეთავში გავაერთიანებ რომ ამ ინსტრუქციის მიყოლა გაგიმარტივდეთ. ამ ეტაპისთვის შაბლონის მიხედვით უნდა გქონდეთ შექმნილი თითოეული კომპონენტის დირექტორია შესაბამისი `forms.py` ფაილებით:

#### myproject/students/forms.py

```python
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    name = StringField('სტუდენტის სახელი:')
    submit = SubmitField('სტუდენტის დამატება')

class DelForm(FlaskForm):
    id = IntegerField('სტუდენტის უნიკალური იდენტიფიკატორი:')
    submit = SubmitField('სტუდენტის წაშლა')

```

#### myproject/teachers/forms.py

```python
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):

    name = StringField('მასწავლებლის სახელი:')
    student_id = IntegerField("სტუდენტის იდენტიფიკატორი: ")
    submit = SubmitField('მასწავლებლის დამატება')

```

### myproject/<component>/views.py

view ფაილების დამატება ბლუპრინტში. შეგვიძლია შემდეგ საფეხურებად ჩავშალოთ:

1. ავაწყოთ view ფაილი რომელიც შაბლონის და ფუნქციონალის დაკავშირებაზეა პასუხისმგებელი
2. ჩავამატოთ Blueprints-ები
3. დავარეგისტრიროთ Blueprint-ები
4. დავუკავშიროთ `app.py`-ს
5. ჩავამატოთ მისამართები `base.html`-ის navbar-ში

პროცესი უნდა დავიწყოთ ბლუპრინტის და სხვა საჭირო რესურსების შემოტანით:

```python
# ფლასკ აპლიკაციის ხელსაწყოების შემოტანა
from flask import Blueprint, render_template, redirect, url_for
# შაბლონში ბაზასთან სამუშაო ფუნქციონალის ჩასაშენებლად
from myproject import db
# ასევე დაგვჭირდება მოდელი, რომლის მიხედვითაც ვაწყობთ ამ ფუნქციონალს
from myproject.models import <ModelName>
# და საბოლოოდ ფორმები რომელიც გვინდა ვებ გვერდში გამოვიყენოთ
from myproject.<component>.forms import <FormFields>
```

ამის შემდგომ დაგვჭირდება კომპონენტის Blueprints ობიექტის შექმნა:

```python
component_blueprint = Blueprint('<component_name>', __name__, template_folder='templates/<component_name>')
```

საბოლოოდ რჩება ფუნქციონალის მისამართზე მიმაგრება.

routing-ში განსხვავება ისაა რომ app ის მაგივრად ახალ მისამართს ჩვენს component_blueprint ობიექტზე ვამატებთ. შესაბამისად მარშუტის სტრუქტურა ასეთი იქნება:

```python
@component_blueprint.route('/add', methods=['GET', 'POST'])
```

სწორედ ამ ობიექტებს დავაკავშირებთ app.py -სთან მთელი თავისი რესურსით/მეთოდებით. შესაბამისად მივიღებთ ორ ფაილს:

#### myproject/students/views.py

```python
from flask import Blueprint,render_template,redirect,url_for
from myproject import db
from myproject.students.forms import AddForm,DelForm
from myproject.models import Student

students_blueprint = Blueprint('students',
                              __name__,
                              template_folder='templates/students')

@students_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data

        # Add new Student to database
        new_student = Student(name)
        db.session.add(new_student)
        db.session.commit()

        return redirect(url_for('students.list'))

    return render_template('add.html',form=form)

@students_blueprint.route('/list')
def list():
    # Grab a list of students from database.
    students = Student.query.all()
    return render_template('list.html', students=students)

@students_blueprint.route('/delete', methods=['GET', 'POST'])
def delete():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        student = Student.query.get(id)
        db.session.delete(student)
        db.session.commit()

        return redirect(url_for('students.list'))
    return render_template('delete.html',form=form)

```

#### myproject/teachers/views.py

```python
from flask import Blueprint,render_template,redirect,url_for
from myproject import db
from myproject.models import Teacher
from myproject.teachers.forms import AddForm

teachers_blueprint = Blueprint('teachers',
                              __name__,
                              template_folder='templates/teachers')

@teachers_blueprint.route('/add', methods=['GET', 'POST'])
def add():

    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        student_id = form.student_id.data
        # Add new teacher to database
        new_teacher = Teacher(name,student_id)
        db.session.add(new_teacher)
        db.session.commit()

        return redirect(url_for('students.list'))
    return render_template('add_teachers.html',form=form)

```

### myproject/<component>/templates/<component>

შაბლონებში შეგვიძლია მოვათავსოთ ნებისმიერი ის html შაბლონი, რომელიც ამ კომპონენტთან სამუშოდ დაგვჭირდება. ილუსტრირებისთვის წინა მაგალითიდან გადმოვიტანოთ სტუდენტ კომპონენტთან სამუშაო შაბლონები.

### students/templates/students/

#### add.html

```html
{% extends "base.html" %} {% block content %}
<div class="jumbotron">
  <h1>სტუდენტის დამატება</h1>
  <p>სტუდენტის დამატება ხდება შემდეგი ფორმიდან:</p>
  <form method="POST">
    {{ form.hidden_tag() }} {{ form.name.label }} {{ form.name() }} {{
    form.submit() }}
  </form>
</div>
{% endblock %}
```

#### delete.html

```html
{% extends "base.html" %} {% block content %}
<div class="jumbotron">
  <h1>გსურთ სტუდენტის წაშლა?</h1>
  <p>შეავსეთ ფორმა სტუდენტის იდენტიფიკატორით</p>
  <form method="POST">
    {# This hidden_tag is a CSRF security feature. #} {{ form.hidden_tag() }} {{
    form.id.label }} {{ form.id() }} {{ form.submit() }}
  </form>
</div>
{% endblock %}
```

#### list.html

```html
{% extends "base.html" %} {% block content %}
<div class="jumbotron">
  <h1>იხილეთ ბაზაში დარეგისტრირებულ სტუდენტთა სია</h1>
  <ol>
    {% for student in students %}
    <ul>
      {{ student.id }} {{ student }}
    </ul>
    {% endfor %}
  </ol>
</div>
{% endblock %}
```

### /teachers/templates/teachers

#### add.html

```html
{% extends "base.html" %} {% block content %}
<div class="jumbotron">
  <h1>მასწავლებლის დამატება</h1>
  <p>მოსწავლის დამატება შეგიძლიათ ფორმიდან:</p>
  <form method="POST">
    {# This hidden_tag is a CSRF security feature. #} {{ form.hidden_tag() }} {{
    form.name.label }} {{ form.name() }}<br />
    {{ form.student_id.label }} {{ form.student_id() }}<br />
    {{ form.submit() }}
  </form>
</div>
{% endblock %}
```

## დამატებითი რესურსები:

- [Use a Flask Blueprint to Architect Your Applications](https://realpython.com/flask-blueprint/)
- https://exploreflask.com/en/latest/blueprints.html
- https://flask.palletsprojects.com/en/1.1.x/blueprints/
- https://flask.palletsprojects.com/en/1.1.x/tutorial/views/
