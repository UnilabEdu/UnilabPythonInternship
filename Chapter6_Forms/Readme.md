# ფორმებთან მუშაობა Flask-ის დახმარებით



ამ თავში ვნახავთ თუ როგორ არის შესაძლებელი ფუნქციონალური ფორმების გამართვა ფლასკის მეშვეობით. ამაში WTForms დაგვეხმარება.
მანამდე კი გავეცნოთ მთავრ საფეხურებს, რომელსაც განვახორციელებთ:

> - დავაყენებთ secret key-ს კონფირგურაციას უსაფრთხოებისთვის
> - შევქმნით WTForm კლასს
>   - შევქმნით შესაბამის არეებს ფორმის თითოეული ნაწილისთვის
> - გავმართავთ View Function-ს
>   - დავამატებთ მეთოდებს `methods = ['GET','POST']`
>   - შევქმნით Form Class
>   - დავამუშავებთ form submission-ს

## [WTForms](https://wtforms.readthedocs.io/en/2.3.x/)

WTForms პითონში ვებ დეველოპმენტზე გათვლილი ფორმების ვალიდაციისა და რენდერის ბიბლიოთეკაა. ის თავსებადია ნებისმიერ ვებ ფრიმვორკთან ან ძრავის შაბლონთან.
WTForms-ის გარშემო არის შექმნილი ბიბლიოთეკები, რომელიც დაგვეხმარება ჩვენს არჩეულ ფრიმვორკში მის მოთავსებაში.

### [WTForms ინსტალაცია](https://pypi.org/project/WTForms/)

ბიბლიოთეკის ინსტალაცია შესაძლებელია [pip](http://www.pip-installer.org/) მენეჯერის გამოყენებით:

```python
pip install WTForms
```

## [FlaskWTF](https://flask-wtf.readthedocs.io/en/stable/)

FlaskWTF არის Flask-ისა და WTForms-ის ინტეგრაცია, რომელიც აერთიანებს ისეთ შესაძლებლობებს როგორიცაა ფაილების ატვირთვა ან CAPTCHA.

![FlaskWTF](https://flask-wtf.readthedocs.io/en/stable/_static/flask-wtf.png)

### [FlaskWTF ინსტალაცია](https://flask-wtf.readthedocs.io/en/stable/install.html)

ბიბლიოთეკის ინსტალაცია შესაძლებელია [pip](http://www.pip-installer.org/) მენეჯერის გამოყენებით:

`pip install Flask-WTF`

## [ფორმის შექმნა](https://flask-wtf.readthedocs.io/en/stable/form.html#creating-forms)

### [შესავალი](https://flask-wtf.readthedocs.io/en/stable/quickstart.html#creating-forms)

ბიბლიოთეკის გამოსაყენებლად უნდა შემოვიტანოთ შესაბამისი ბიბლიოთეკა აპლიკაციაში:

```python
from flask_wtf import FlaskForm
```

ამის შემდგომ შეგვიძლია გამოვიყენოთ WTForms ბიბლიოთეკა შესაბამისი ფორმის შემოსატანად. მაგალითად სტრიგ მონაცემის ამოსაღები ფორმისთვის
შეგვიძლია გამოვიყენოთ `StringField` :

```python
from wtforms import StringField
```

როგორც ვახსენეთ პირველ საფეხური იქნება secret key. უსაფრთხოების შესაძლებლობების გამოსაყენებლად, მას შემდეგ რაც შევქმნით Flask app ობიექტს, შეგვიძლია კონფიგურაციაში გავუწეროთ Secret Key.

```python
app.config['SECRET_KEY'] = <Secret_Key>
```

მოგვიანებით ვნახავთ როგორ შეგვილია Secret Key მოვათავსოთ environmental ცვლადში მეტი დაცულობისთვის.

ამ ეტაპისთვის ჩვენი კოდი Flask და FlaskWTFთან ერთად, დაახლოებით ასე უნდა გამოიყურებოდეს (დამოკიდებულია თუ რა ელემენტები შემოგაქვთ ბიბლიოთეკებიდან).

```python
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SEKRET_KEY'] = "Mellon"
```

### ერთეული ელემენტის მაგალითი

ფორმის ასაწყობად პითონში გამოვიყენებთ კლასებს და კლასების მემკვიდრეობის თვისებას.
ყოველ ფორმისთვის შექმნილ კლასს პარამეტრად გადავცემთ FlaskForm-ს რაც ამ კლასს ფორმის თვისებებს მიანიჭებს. ფორმის ელემენტებს ისე ვქმნით როგორც კლასის ატრიბუტებს.

```python
class FormName(FlaskForm):
    information = StringField("What kind of information are you looking for?")
    submit = SubmitField('submit')
```

### ფორმის მისამართში შემოტანა

ავაწყოთ ახალი როუთი რომელზეც გვსურს ფორმის გამოყენება.

```python
@app.route('/', methods=['GET', 'POST'])
def index():

    information = None

    form = FormName()

    if form.validate_on_submit():

        information = form.information.data
        form.information.data = ''

    return render_template('demo.html', form = form, information = information)

```

> 1. როუთში ვქმნით ფორმის ობიექტს `form = FormName()`.
> 2. `if form.validate_on_submit():` პირობით ვამოწმებთ მოთხოვნა ამ როუთზე მოვიდა თუ არა ამ ფორმის დასაბმითებით.
> 3. თუ ეს პირობა ჭეშმარიტია, გვეძლევა შესაძლებლობა ფორმის ელემენტებიდან ამოვიღოთ ინფორმაცია data მეთოდის გამოყენებით:
>    `<form.attribute_name.data>`.
> 4. ამოღებულ ინფორმაციას გადავცემთ html შაბლონს და ვტვირთავთ სრულ გვერდს `render_template()` მეთოდის გამოყენებით

##### საბოლოო Flask აპლიკაციის კოდი:

```python
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = "Mellon"

class UsernameForm(FlaskForm):
    username = StringField("Username: ")
    submit = SubmitField('submit')

@app.route('/', methods=['GET', 'POST'])
def index():

    username = None

    form = UsernameForm()

    if form.validate_on_submit():

        username = form.username.data
        form.username.data = ''

    return render_template('demo.html', form = form, username = username)

if __name__ == '__main__':
    app.run(debug = True)
```

### html-თან დაკავშირება - demo.html

```jinja
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.username.label }} {{ form.username() }}
        {{ form.submit() }}
    </form>
```

როგორც ხედავთ შემოტანილ form ობიექტის ატრიბუტებს ვიყენებთ ფორმის რენდერისათვის. გასათვალისწინებელია, რომ form ობიექი შეიცავს როგორც ჩვენს მიერ ხელით გაწერილ,
ისე FlaskForm კლასიდან მემკვიდრეობით მიღებულ ატრიბუტებს.

- `{{ form.hidden_tag() }}` - FlaskForm კლასის ატრიბუტია და გვეხმარება ფორმის უსაფრთხოების გამართვაში
- `{{ form.username.label }}` - მნიშვნელობად მიიღებს StringField-ისთვის გადაცემულ პირველ პარამეტრს, რომელიც გვინდოდა რომ ფორმის შევსებისას წარწერად გამოჩენილიყო
- `{{ form.username() }}` - აგენერირებს უშუალოდ ფორმას შესაბამისი პარამეტრისთვის
- `{{ form.submit() }}` - აგენერირებს საბმით ღილაკის ფორმას

## [Forms / Form Fields](https://wtforms.readthedocs.io/en/2.3.x/fields/)

### შესავალი

თითქმის ყველა [HTML input თეგს აქვს შესაბამისი WTForms კლასი](https://wtforms.readthedocs.io/en/2.3.x/fields/#basic-fields) და შესაბამისად FlaskWTF-ის მხარდაჭერა
რომლის პროექტში შემოტანაც არის შესაძლებელი.
WTForms ასევე აქვს ვალიდატორიც რომლის ჩასმაც შესაძლებელია ფორმებში. ვალიდატორებს შეუძლიათ შეამოწმონ ფორმაში შეტანილი
მონაცემი, მაგალითად ფორმატის მიხედვით, არის თუ არა შევსებული ფორმა და ა.შ.

WTForms -დან შეგვიძლია გამოვიყენოთ Flask-ის session ობიექტი რათა შევინახოთ ფორმიდან აღებული ინფორმაცია და გამოვიყენოთ
მოგვიანებით სხვა შაბლონზე მუშაობისას. მოგვიანებით კი შევძლებთ ამ ინფორმაციის სესიის მაგივრად მონაცემთა ბაზაში შენახვას.

გავამზადოთ სამუშაო გარემო და შემოვიტანოთ საჭირო ინსტრუმენტები:

```python
from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateTimeField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
```

### ფორმების მაგალითები

უკვე გავიცანით StringField ფორმის ინპუტი. ვნახოთ სხვა ტიპის მაგალითები wtforms-იდან.

| wtformField                                                                                   | html თეგი                 | მაგალითი                                                                                                                |
| --------------------------------------------------------------------------------------------- | ------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `StringField()`                                                                               | `<input type="text">`     | `name = StringField('Full Name')`                                                                                       |
| `BooleanField()`                                                                              | `<input type="checkbox">` | `like = BooleanField('კმაყოფილი ხართ სერვისით?')`                                                                       |
| `RadioField()`                                                                                | `<input type="radio">`    | `product = RadioField('გთხოვთ აირჩიოთ სასურველი პროდუქტი:' , choices=[('value','lable'),...])`                          |
| [`SelectField()`](https://wtforms.readthedocs.io/en/2.3.x/fields/#wtforms.fields.SelectField) | `<select></select>`       | `food_choice = SelectField(u'Pick Your Favorite Food:', choices=[('chi', 'Chicken'), ('bf', 'Beef'),('fish', 'Fish')])` |
| `TextField()`                                                                                 | `<textarea><textarea/>`   | `feedback = TextField()`                                                                                                |
| `SubmitField()`                                                                               | `<input type="submit">`   | `SubmitField('გაგზავნა')`                                                                                               |

### [ვალიდატორები](wtforms.simplecodes.com/docs/0.6.2/validators.html)

`from wtforms.validators import DataRequired`

ვალიდატორი აკვირდება ფორმის ელემენტს და ამოწმებს მას წინასწარ გაწერილ კრიტერიუმებთან შესაბამისობაზე. მაგალითად არის თუ არა იმეილი სწორი ფორმატით შეყვანილი, ან აკმაყოფილებს თუ არა შეყვანილი პაროლი უსაფრთხოების სტანდარტებს.
wtforms გვთავაზობს როგორც ჩაშენებულ ვალიდატორებს, ასევე შესაძლებლობას ავაწყოთ ჩვენი ვალიდატორები.

`name = StringField('Full Name', [DataRequired(), validators.length(max=10)])`

#### მაგალითები

| ვალიდატორი               | გამოყენება                                                        |
| ------------------------ | ----------------------------------------------------------------- |
| `DataRequired() `        | ამოწმებს შევსებულია თუ არა ველი                                   |
| ` length(min=2, max=15)` | ამოწმებს შეყვანილი ინფორმაციის ზომას                              |
| `Email() `               | ამოწმებს არის თუ არა შეყვანილი მონაცემი მეილის სტილის             |
| `EqualTo(fieldname) `    | ადარებს შეყვანილ ინფორმაციას მეორე ფორმის (fieldname) ინფორმაციას |

#### message პარამეტრი

ვალიდატორს შეგიძლიათ პარამეტრად გადასცეთ message მნიშვნელობა, რომელსაც გამოიყენებთ ვალიდაციის ვერ გავლის შემთხვევაში. მაგალითად
თუ პაროლის შეცვლის ფუნქციონალს ვაკეთებთ, სადაც გვინდა მომხმარებელმა გაიმეოროს ახალი პაროლი რადგან დარწმუნდეს მის სისწორეში, შეგვიძლია
გამოვიყენოთ მსგავსი შეტყობინება:

```python
class ChangePassword(Form):
    password = PasswordField('New Password', [Required(), EqualTo('confirm', mesage='Passwords must match')])
    confirm  = PasswordField('Repeat Password')
```

## [session](https://flask.palletsprojects.com/en/1.1.x/api/#sessions)

ფლასკი ქმნის stateless servers, რაც ნიშნავს რომ მონაცემების გადაცემა ან გამოყენება მოთხოვნებს შორის შედარებით რთული ამოცანა ხდება.
Flask session შეუძლია შეინახოს ინფორმაცია პროგრამის მუშაობის სამომავლო ეტაპზე გამოსაყენებლად. გაბსხვავებით ქუქიებისგან, სესიის შემთხვევაში მონაცემების შენახვა-დამუშავება ხდება სერვერის მხარეს.
შესაბამისად ის გვაძლევს შესაძლებლობას ინფორმაცია შევინახოთ და გამოვიყენოთ მოთხოვნიდან მოთხოვნამდე დაუკარგავად.

თუმცა გაითვალისწინეთ რომ სესიაში შენახული ინორმაცია არ ნიშნავს რომ მყარად შენახული ინფორმაციაა, როგორც მაგალითად მონაცემთა ბაზაში მოთავსებული ინფორმაცია. წარმოიდგინეთ სესია როგორც მონაცემის დროებითი საცავი.

ამ სერვისის გამოსაყენებლად აუცილებელია SECRET_KEY კონფიგურაციის გაწერა ფლასკ აპლიკაციაში. მომხმარებელი შეძლებს სესიის ინფორმაციის ნახვას, თუმცა ვერ შეძლებს მასზე ზემოქმედებას (ცვლილებას, წაშლას) საიდუმლო გასაღების გარეშე.
სესიაზე წვდომისთვის შეგვიძლია გამოვიყენოთ session ობიექტი, რომელსაც დაახლოებით dict ტიპის მონაცემივით გამოიყენებთ.

ბიბლიოთეკის შემოსატანად: `from Flask import session`

```python
session['session_variable_name'] = data_to_store
```

## სამუშაო მაგალითი

ზემოთ განხილული თემებით საბოლოოდ ავაწყოთ ვებ სერვისი რომელიც ამ თავში განხილული შესაძლებლობეიბს დემონსტრირებაში დაგვეხმარება.

### 1. შენივიტანოთ საჭირო რესურსები app.py-ში

### 2. შევქმნათ FormField ობიექტი

```python
class InfoForm(FlaskForm):
    name = StringField('გთხოვთ შეიყვანოთ მომხმარებლის სახელი', validators=[DataRequired()])

    safe_distance  = BooleanField("გსურთ უკონტაქტო მიწოდება?")

    payment = RadioField('გადახდის საშუალება?', choices=[('cash','ფული'),('card','ბარათი')])

    food_choice = SelectField(u'აირჩიეთ კერძის ძირითადი ინგრედიენტი',

    choices=[('chi', 'ქათამი'), ('vg', 'ვეჯი'), ('fish', 'თევზი')])

    feedback = TextAreaField()
    submit = SubmitField('შეკვეთა')

```

### 3. შევქმნათ მისამართი რესურსზე

შევქმნათ მისამართი რომელშიც შემოვიტანთ ჩვენს მიერ გამზადებულ ფორმას, დადასტურების შემთხვევაში ამოვიღებთ მონაცემებს ფორმიდან და გამოვიტანთ შესაბამის შაბლონზე.

```python

@app.route('/', methods=['GET', 'POST'])
def index():

    # შევქმნათ ობიქტი ჩვენს მიერ გაწერილი ფორმით
    form = InfoForm()

    # თუ ფორმა დასტურდება
    if form.validate_on_submit():
        # მოვათავსოთ სესიაში ფორმებიდან ამოღებული მონაცემები

        session['name'] = form.name.data
        session['safe_distance'] = form.safe_distance.data
        session['payment'] = form.payment.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data

        return redirect(url_for("thankyou"))


    return render_template('base.html', form=form)

```

შეკვეთის დასტურის შემთხვევაში გამოსაჩენი გვერდის მისამართი:

```python
@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')
```

### 4. გავამზადოთ ვებ შაბლონები home.html და thankyou.html

#### home.html

```jinja2
{% extends "base.html" %}
{% block content %}

    <h1>შეუკვეთე გემრიელობა</h1>
    <form  method="POST">
        {# This hidden_tag is a CSRF security feature. #}
        {{ form.hidden_tag() }}
        {{ form.name.label }} {{form.name}}
        <br>
        {{ form.safe_distance.label}} {{form.safe_distance}}
        <br>
        {{form.food_choice.label}}{{form.food_choice}}
        <br>
        {{form.payment.label}}{{form.payment}}
        <br>
        <h3>რამეს ხომ არ დაამატებდით?</h3>
        <br>
        {{form.feedback}}
       <br>
        {{ form.submit() }}
    </form>

{% endblock %}

```

#### thankyou.html

```jinja2
<h3>მადლობა {{session['name']}}, თქვენი შეკვეთა მიღებულია:</h3>
<p>შეკვეთის შეჯამება: </p>
<code>
<ul>
  <li>Neutered: {{session['safe_distance']}}</li>
  {# Note, this saves the payment key, not the form value!!! #}
  <li>payment: {{session['payment']}}</li>
  <li>Food: {{session['food']}}</li>
  <li>Feedback: {{session['feedback']}}</li>
</ul>
</code>
```

## alerts

დინამიურ ვებ სერვისზე მუშაობისას ხშირად გვჭირდება გარკვეული პროცესის შესრულებისას მომხმარებელთან არაპირდაპირი კომუნიკაცია. შეიძლება საჭირო გახდეს
მომხმარებლისთვის პროგრამის მუშაობის პროცესზე ინფორმაციის მიწოდება, შეცდომის შესახებ ინფორმაციის გამოტანა, გარკვეული გაფრთხილების ან ინსტრუქციის მიცემა.

მსგავსი ინფორმაცია როგორც წესი არ არის შაბლონის აქტიური წევრი და მისი გამოტანა დინამიურად გვჭირდება კონკრეტული ამოცანის შეტყოვინებიდან გამომდინარე.
ამისთვის შეგვიძლია ფლეშ შეტყობინებები გამოვიყენოთ, რომლის წაკითხვის შემდგომ შეძლებს მომხმარებელი დახუროს შეტყობინების ველი და განაგრძოს მუშაობა.

Flask ამ პროცესს საკმაოდ ამარტივებს ჩაშენებული [flash](https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/) ფუნქციონალით. ხოლო გამოტანილი
შეტყობინებისთვის სასიამოვნო ვიზუალის შესაქმნელად [Bootstrap-ის შეტყობინებების კომპონენტებს](https://getbootstrap.com/docs/4.0/components/alerts/) გამოვიყენებთ.

### მაგალითი

ავაწყოთ აპლიკაცია, რომელსაც გამოაქვს შეტყობინება შევსებული ფორმის დასაბმითების შემთხვევაში `flash()`-ის გამოყენებით.

```python
from flask import Flask, render_template, flash, session, redirect, url_for
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
        flash("შენ ახლახანს დააჭირე")

        return redirect(url_for('index'))
    return render_template('base.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
```

იმ შემთხვევაში თუ `validate_on_submit()` პირობა სრულდება შესრულდება `flash("შენ ახლახანს დააჭირე")`.

#### შაბლონის მხარე

ვნახოთ როგორ შეგვიძლია გამოვიყენოთ ეს ფუნქციონალი ვებ გვერდის მხარეს, შეტყობინების გამოსატანად.

იმისთვის რომ ფუნქციონალური (გაქრობის შესაძლებლობით) შეტყობინების გამოყენება შევძლოთ, აუცილებელია შემოვიტანოთ შაბლონში Bootstrap
jQuery რესურსებიც.

```html
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
```

ავაწყოთ ლოგიკა რომელიც გამოაჩენს შეტყობინებას საჭირო დროს
`home.html`

```html
{# get_flashed_messages() ავტომატურად იღებს flash()-ის პარამეტრებს #} {% for msg
in get_flashed_messages() %}
<div class="alert alert-warning alert-dismissible fade show" role="alert">
  <button
    type="button"
    class="close"
    data-dismiss="alert"
    aria-label="Close"
    class="fade close"
  >
    <span aria-hidden="true">&times;</span>
  </button>
  {{msg}}
</div>
{% endfor %}

<form method="POST">{{ form.hidden_tag() }} {{ form.submit() }}</form>
```

## [ფაილის ფორმა](https://flask-wtf.readthedocs.io/en/stable/form.html#module-flask_wtf.file)

როდესაც ვქმნით ახალ ფორმას, თუ ფორმაში არ არის ფაილის ატვირთვა როგორც წესი არ გვჭირდება enctype-ის გაწერა. სახელმძღვანელოდ:

application/x-www-form-urlencoded: არის default და საუკეთესო მნიშვნელობა ფორმისთვის თუ არ ვიყენებთ ფაილებს.
multipart/form-data: ფორმატი არის აუცილებელი თუ მინიმუმ ერთი ფაილთან სამუშაო ფორმა მაინც გვაქვს პროგრამაში.

თვითონ ფაილის ატვირთვის შრე ჩვეულებრივი input ელემენტია ტიპით file.

### მაგალითი

```html
<form method="POST" action="" enctype="multipart/form-data">
  <input type="file" name="file" />
  <input type="submit" value="Submit" />
</form>
```

ფაილ ტიპის ინპუტ შრეს შეგვიძლია ორი საკმაოდ პრაქტიკული ატრიბუტი დავუმატოთ: `multiple` რომელიც შეგვიძლია გამოვიყენოთ თუ გვინდა პარალელურად
რამოდენიმე ფაილის ატვირთვა დავუშვათ და `accept` რომელიც ერთგვარი ფილტრი/ ვალიდატორი იქნება ფორმისთვის.

```html
<input type="file" name="file" multiple />
<input type="file" name="doc_file" accept=".doc,.docx" />
<input type="file" name="image_file" accept="image/*" />
```

### სერვერის მხარე

შევქმნათ პროექტის მთავარ დირექტორიაში ქვედირექტორია /uploads სადაც მოვათავსებთ ატვირთულ ფაილებს.

ფაილებთან სამუშაოდ დაგვჭირდება flask_wtf-დან ხელსაწყოების შემოტანა პროექტში. ასევე გამოვიყენებთ werkzeug.utils-დან secure_filename რაც დაგვიცავს მავნე მომხმარებლის
მიერ საზიანო ფაილის ატვირთვისას.

შევქმნათ ფლასკის კოდის მაგალითი თუ როგორ შეგვიძლია ავტვირთოთ სურათი სერვერზე.

#### ბიბლიოთეკები

```python
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename

class UploadForm(FlaskForm):
    file = FileField()

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm()

    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        form.file.data.save('uploads/' + filename)
        return redirect(url_for('upload'))

    return render_template('upload.html', form=form)

```

შესაბამისად save მეთოდს თუ გადავცემთ პარამეტრად ფაილის შესანახ მისამართს ის მოათავსებს ატვირთულ ფაილს შესაბამის დირექტორიაში შესაბამისი დასახელებით.
