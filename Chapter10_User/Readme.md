# მომხმარებელი

## შესავალი

ამ დრომდე ჩვენს მიერ შექმნილ ყველა რესურსზე ღია წვდომა გვაქვს. ეს ნიშნავს რომ ნებისმიერი ვებ გვერდის თუ API-ს ფუნქციონალის ნახვა და გამოყენება ყველასთვის ღიაა. ხშირ შემთხვევაში კი გვჭირდება რომ გარკვეული ფუნქციონალი მხოლოდ რეგისტრირებული მომხმარებლისთვის გამოვაჩინოთ. შესაძლებელია რეგისტრირებული მომხმარებლებიც დავყოთ ქვეჯგუფებად და მივანიჭოთ მათ შესაბამისი პრივილეგიები და შესაძლებლობები.

ამ თავის ძირითადი მისანია გავეცნოთ მომხმარებლის ავტორიზაციას და აუთენტიფიკაციას. პროცესში ვისწავლით პაროლის ჰეშირებას, ფლასკის აუტორიზაციის და აუტენთიფიკაციის ბიბლიოთეკების გამოყენებას.

## მომხმარებლის ავტორიზაცია და პაროლი

თუ საიტზე ვაპირებთ ავტორიზაციის ჩაშენებას ეს ნიშნავს, რომ მომხმარებელს შესაძლებლობას ვაძლევთ გაიაროს რეგისტრაცია და შექმნას თავისი ციფრული ანგარიში, რომლის დახმარებითაც შეძლებს გარკვეულ პროცესებზე მოიპოვოს წვდომა.

იმისთვის რომ მომხმარებლის ანგარიში დავიცვათ და ანგარიშის მართვაზე მხოლოდ მომხმარებელს ჰქონდეს წვდომა, საჭიროა გარკვეული ავტორიზაციის ფორმის გამოყენება. ყველაზე გავრცელებული ფორმა მომხმარებლის **უნიკალური იდენტიფიკატორისა** და მხოლოდ მისთვის ცნობილი **პაროლის** გამოყენებით ავტორიზაციაა. ამ პროცესს log in ანუ შესვლის ფორმის გავლით გავდივართ.

ფორმაში შევსებული მონაცემის გადასამოწმებლად აუცილებელია სერვერის მხარესაც გვქონდეს შენახული მომხმარებლის მიერ რეგისტრაციის დროს არჩეული **იდენტიფიკატორი** (ხშირ შემთხვევაში _username_-მომხმარებლის სახელი) და პაროლი (password). რადგან მომხმარებლის პაროლი ერთ-ერთი ყველაზე ფაქიზი მონაცემია რაც მომხმარებლის მთელს ანგარიშზე წვდომის მოსაპოვებლად გამოიყენება, აუცილებელია მისი დაცვა შევძლოთ, იმ შემთხვევაშიც კი თუ ვინმე ჩვენი მონაცემთა ბაზიდან მონაცემის ამოღებას შეძლებს. შესაბამისად, უსაფრთხოების მიზნებისთვის, არასდროს არ უნდა შევინახოთ ტექსტი პირდაპირი სახით, იმ სტრინგად როგორც ის მომხმარებელმა შეავსო.

ინფორმაციის დასაშიფრად შეგვიძლია გამოვიყენოთ **hash** ფუნქცია. ჰაშირება ნიშნავს ისეთი ალგორითმის გამოყენებას, რომელიც იღებს დოკუმენტს (ჩვენს შემთხვევაში პაროლის შიგთავსს) და უკან გვიბრუნებს უსაფრთხოდ დაშიფრულ ფაილს. ჰაშირებული ფაილი უსაფრთხოა რადგან ადამიანისთვის ამგვარი ფაილის შიგთავსი არაინფორმაციულია. საბედნიეროდ უკვე არსებობს ჰაშირების უამრავი სხვადასხვა ალგორითმი და ბიბლიოთეკა რომლის გამოყენებაც პროექტში შეგვიძლია.

შესაბამისად ჩვენ ჰაშირების ფუნქციის გამოყენებით დავშიფრავთ რეგისტრაციის დროს მომხმარებლის მიერ შეყვანილ პაროლს და ისე მოვათავსებთ მონაცემთა ბაზაში. მომხმარებლის ყოველი ავტორიზაციისას შეყვანილ პაროლსაც მსგავსი ალგორითმით გავუკეთებთ ჰეშირებას და შევადარებთ მომხმარებლის იდენტიფიკატორის გასწვრივ დამახსოვრებულ ჰაშირებულ პაროლს. დამთხვევის შემთხვევაში შეგვიძლია ჩავთვალოთ რომ მომხმარებელმა ავტორიზაცია წარმატებით გაიარა.

ამისთვის ორი საკმაოდ გამოსადეგი ბიბლიოთეკები გვაქვს პითონ გარემოში, ჩვენ მათგან ორს განვიხილავთ. ესენია:

- Bcrypt
- Werkzeug

ორივე საკმაოდ პოპულარულია, ხშირად გამოიყენება Flask აპლიკაციებში და საკმაოდ ჰგავს ერთმანეთს. ასე რომ არჩევანი თქვენზეა, თუ რომელს გამოიყენებთ საბოლოოდ პროექტში.

## Bcrypt

<img src="https://i.ytimg.com/vi/r1Iygf-rRdE/maxresdefault.jpg" alt="Argon2 Password Hashing Node.js | BCrypt Alternative - YouTube" style="zoom:20%;" />

_bcrypt_ არის პაროლის ჰაშირების ფუნქცია რომელიც Niels Provos და David Mazières დიზაინის მიხედვით შეიქმნა და გამოსაყენებლად 1999 გამოჩნდა, თუმცა დღემდე საკმაოდ აქტიურად გამოიყენება. მისი გამოყენება შესაძლებელია პითონის აპლიკაციებშიც, შესაბამისი ბიბლიოთეკის დაყენების შემდგომ:

```bash
pip install bcrypt
```

თუმცა ჩვენ გამოვიყენებთ უშუალოდ Flask-ზე ოპტიმიზირებულ ვერსიას, რომელსაც იოლად ჩავაშენებთ ჩვენს flask აპლიკაციაში:

```
 pip install flask-bcrypt
```

პროექტში შემოსატანად კი დგვჭირდება შემდეგი პითონის ინსტრუქციის გაწერა:

```python
from flask_bcrypt import Bcrypt
```

პროექტში Bycrpt-ის გამოსაყენებლად უნდა შევქმნათ შესაბამისი ჰეშერ ობიექტი. მისი დახმარებით შევძლებთ ნებისმიერი მონაცემის ჰაშირებას. ჰაშირების პროცესში დაგვეხმარება `generate_password_hash(password='string_to_hash')` მეთოდი.

მაგალითად:

```python
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

password = "bestkeptsecret"

hashed_pass = bcrypt.generate_password_hash(password=password)

print(f'Hashed_Pass: {hashed_pass}')
```

დაგვიბრუნებს სტრინგის ჰაშირებულ ვერსიას:

`Hashed_Pass: b'$2b$12$m3DOb4ospynwqO.TEb6bHeJh3nWgenyRjpDA6LstfsjoOBpVzW3HG'`

ამრიგად დაშიფრული პაროლის შენახვა უკვე შესაძლებელია ბაზაში, რადგან როგორც ხედავთ ის ადამიანისთვის აბსოლუტურად არაინფორმატიულია.

მომხმარებლის მიერ შეყვანილი პაროლის გადასამოწმებლად, ისევ Bcrypt ბიბლიოთეკიდან გამოვიყენებთ `check_password_hash(hashed_pass, 'user_typed_password')`. როგორც ხედავთ მეთოდს არგუმენტებად უნდა გადავცეთ შესადარებელი პარამეტრები. მეთოდი უკან დაგვიბრუნებს True/False მნიშვნელობებს იმის მიხედვით სწორია თუ არა მომხმარებლის შეყვანილი მონაცემი.

## Werkzeug

_werkzeug_ German noun: “tool”. Etymology: _werk_ (“work”), _zeug_ (“stuff”)

![Werkzeug — Werkzeug Documentation (1.0.x)](https://werkzeug.palletsprojects.com/en/1.0.x/_static/werkzeug.png)

Werkzeug-ის გამოყენებაც იდენტურად ხდება. თუ ამ ეტაპზე არ გაქვთ ბიბლიოთეკა შეგიძლია გადმოწეროთ მენეჯერის დახმარებით:

```bash
pip install Werkzeug
```

Werkzeug იყენებს გარე ბიბლიოთეკებს და იდეალურად მუშაობს Flask -თან.

ჩვებ შემოგვაქვს მისი security ნაკრებიდან პაროლის ჰაშირების ხელსაწყოებს: `generate_password_hash` და `check_password_hash`.

```python
from werkzeug.security import generate_password_hash, check_password_hash
```

მნიშვნელოვანი განსხვავება `bcrypt`-ისგან არის რომ არ გვჭირდება დამატებითი ობიექტის შექმნა ჰაშირების მეთოდების გამოსაყენებლად. ბიბლიოთეკიდან პირდაპირ შემოგვაქვს მეთოდები რომელიც ფუნქციისამებრ შეგვიძლია გამოვიყენოთ.

მაგალითად:

### პაროლის ჰაშირებისთვის

```python
hashed_pass = generate_password_hash('bestkeptsecret')
print(hashed_pass)
```

> `Hashed_Pass: pbkdf2:sha256:150000$oFv3Q4NF$fe102689242d740cca5f1cd100c9bb3c31051c63a8df817f9a76dd26c49b6ceb`

### პაროლის შესამოწმებლად

```python
check = check_password_hash(hashed_pass, 'bestkeptsecret')
print(f'Result: {check}')
```

> `Result: True`

## [Flask-Login](https://flask-login.readthedocs.io/en/latest/)

`flask-login` არის ფლასკის დამატებითი ბიბლიოთეკა, რომელიც მომხმარებლის პროფილზე "შესვლის"/აუტენთიფიკაციის ფუნქციონალის ვებ აპლიკაციაში ჩაშენების საფეხურს გაგვიმარტივებს. ის შედგება მარტივად გამოსაყენებელი დეკორატორებისგან რომელითაც სწრაფად და მარტივად ეწყობა მომხმარებლის სხვადასხვა ფუნქციონალი.

გარდა ავტორიზაციისა, Flask-login -ის გამოყენებით შესაძლებელია აქტიური მომხმარებლის სესიაში შენახვა, მომხმარებლის სესიის დაცვა რომ არ მოხდეს ინფორმაციის ქუქიებიდან ამოღება, გვერდებზე დაშვების კონტროლი ...

აპლიკაციაში ბიბლიოთეკის შესაძლებლობების გამოყენება ხდება [`LoginManager`](https://flask-login.readthedocs.io/en/latest/#flask_login.LoginManager) კლასის გამოყენებით. მისი დახმარებით შექმნილი ობიექტით ჩვენ შევძლებთ ბიბლიოთეკის ყველა ფუნქციონალზე წვდომის მოპოვებას:

```python
login_manager = LoginManager()
```

სწორედ მენეჯერი შეიცავს კოდს რომელიც გვეხმარება ჩვენი აპლიკაცია დავაკავშიროთ Flask-Login -თან, მომხმარებლის ამოცანებთან სამუშაოდ. როგორც ვთქვით ეს ასმოცანა შეძლება იყოს მომხმარებლის ვერიფიცირება, მომხმარებლის აღდგენა მისი იდენტიფიკატორით, ავტორიზებული მომხმარებლის გადამისამართება და ა.შ.

მას შემდეგ რაც flask აპლიკაციის ობიექტს შექმნით მისი დაკავშირება მენეჯერთან `init_app()` მეთოდით შეგვიძლია:

```
login_manager.init_app(app)
```

სტანდარტულად, Flask-Login იყენებს სესიას მომხმარებლის ავტორიზაციისთვის. იმისთვის რომ მომხმარებლის ინფორმაცია დავიცვათ, აუცილებელია აპლიკაციას დავადოთ secret key, წინააღმდეგ შემთხვევაში ფლესკი დაგვიბრუნებს შეცდომის შეტყობინებას.

ამ კონფიგურაციის პროცესის სანახავად შეგიძლიათ შეამოწმოთ მაგალით [`__init__.py` მოდულში](#__init__.py)

_Warning:_ Make SURE to use the given command in the “[How to generate good secret keys](https://flask.palletsprojects.com/en/1.1.x/quickstart/#sessions)” section to generate your own secret key. DO NOT use the example one.

## სადემონსტრაციო პროექტის სტრუქტურა

დემონსტრაციისთვის ავაწყოთ ახალი აპლიკაცია. შესაბამისი სტრუქტურით:

```
FlaskApp
|____ myproject
|____ app.py
```

გაითვალისწინეთ, აპლიკაცია და პროექტის საქაღალდე ერთ დონეზეა.

myproject-ში დაგვჭირდება შესაბამისი ფაილების დამატება:

```
myproject
|____ __init__.py
|____ forms.py
|____ modules.py
|____ templates
     |____ base.html
     |____ home.html
     |____ login.html
     |____ register.html
     |____ welcome_user.html

```

### `__init__.py`

როგორც შევთანხმდით აქ ავაწყობთ აპლიკაციას და მის კონფიგურაციას

```python
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


# შევქმნათ login manager ობიექტი
login_manager = LoginManager()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

# გადავცეთ ჩვენი აპლიკაცია login_manager ობიექტს, init_app() მეთოდის გამოყენებით
login_manager.init_app(app)

# მივუთითოთ თუ რომელი view-დან შეძლებს მომხმარებელი საიტზე შესვლას
login_manager.login_view = "login"

```

### `models.py `

ავტორიზაცია არის პროცესი, რომლის დროსაც რეგისტრირებული მომხმარებელი იდენტიფიკატორისა და პაროლის გამოყენებით ადასტურებს საკუთარ თავს. რეგისტრიებული მომხმარებელი ნიშნავს მომხმარებელს რომლის მონაცემებიც (მათ შორის ID და Password) დაცულია მონაცემთა ბაზაში. უკვე ვიცით რომ პაროლის დასაცავად ვშიფრავთ მას Hash ფუნქციით. მოდი შევაჯამოთ ყველა ეს დავალება და ვაქციოთ ის კოდად:

1. შევქმნათ ბაზის მოდელი რომელშიც მოვათავსებთ მომხმარებლის საბაზისო ინფორმაციას:
   - მეილი
   - იდენტიფიკატორი
   - პაროლი
2. ობიექტის შენახვისას გავაკეთოთ პაროლის ჰაშირება
3. შევქმნათ check_password() მეთოდი, რომლითაც შეყვანილ პაროლს შევადარებთ ბაზასი არსებულს

#### 1. ბაზის მოდელის შექმნა

უკვე ვიცით რომ SQLAlchemy-ს დახმარებით ბაზის მოდელის შესაქმნელად გვესაჭიროება ბაზის ობიექტი. სწორედ მისი დახმარებით შეგვიძლია ვაქციოთ კლასი ბაზის მოდელად. შესაბამისად შემოვიტანოთ პროექტიდან `db` ობიექტი და გავწეროთ ბაზის მოდელი:

```python
from myproject import db
from flask_login import UserMixin

class User(db.Model, UserMixin):

    # Create a table in the db
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
```

როგორც ხედავთ flask_login-იდან შემოვიტანეთ `UserMixin`. მისი დახმარებით მომხმარებლის უამრავ ატრიბუთან გვექნება წვდომა რომელიც ბიბლიოთეკაშია ჩაშენებული. `UserMixin` -ის პრაქტიკულ გამოყენებას შემდეგ საფეხურზე ვნახავთ.

#### 2. მომხმარებლის დამატება

`SQLAlchemy` -ის გამოყენებით, ბაზის მონაცემებთან ვმუშაობთ როგორც პითონის ობიექტებთან. პითონში კლასის მიხედვით ობიექტის ერთ-ერთი მარტივი გზა `__init__` მეთოდის გამოყენებაა. სწორედ ამ საფეხურზე, ობიექტის შექმნისას მოვახდენთ პაროლის ჰაშირებას, მის მონაცემთა საცავში ჩაწერამდე. ამისთვის გამოვიყენებ `werkzeug.security` -იდან ჰაშირების მეთოდს:

```python
from werkzeug.security import generate_password_hash,

# in class User:
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)
```

შესაბამისად ობიექტი, ანუ მწკრივი ბაზაში, შეიქმნება ჰაშირებული პაროლით. ამრიგად მომხმარებლის პაროლი ხდება დაცული.

#### 3. პაროლის გადამოწმების მეთოდი

პაროლის გადასამოწმებლად `werkzeug.security` -დან გამოვიყენებთ `check_password_hash()` მეთოდს:

```python
def check_password(self,password):
    return check_password_hash(self.password_hash,password)
```

#### შემოსული მომხმარებელი

მას შემდეგ რაც მომხმარებელი გაივლის ავტორიზაციას ჩვენ შეგვიძლია პროგრამის მსვლელობისას ამოვიღოთ ამ მომხმარებლის მონაცემი სხვადასხვა ამოცანებისთვის. მაგალითად ID, სახელი ან მომხმარებელთა ჯგუფი შეგვიძლია გამოვიყენოთ მომხმარებლის ვებ ვიუების შესაზღუდად ან დასაშვებად.

ყველა ამ შესაძლებლობას, ფლასკის აპლიკაციით შექმნილი `login_manager` მოგცემს. შესაბასმისად ჩვენი პროექტიდან უნდა შემოვიტანოთ მენეჯერის ობიექტი.

#### user_loader

[`user_loader`](https://flask-login.readthedocs.io/en/latest/#flask_login.LoginManager.user_loader) გამოიყენება ავტორიზებული მომხმარებლის ჩასატვირთად. მისი გამოყენებით შეგვიძლია მონაცემთა ბაზიდან ამოვიღოთ მომხმარებლის ობიექტი, მისი ID-ს გამოყენებით. შესაბამისად უნდა ავაწყოთ ფუნქცია რომელსაც გადავცემთ მომხმარებლის იდენტიფიკატორს და დაგვიბრუნებს ამ იდენტიფიკატორის ქვეშ არსებული მომხმარებლის ობიექტს. ეს ყველაფერი კი უნდა შევმოსოთ `user_loader` დეკორატორით:

```python
from myproject import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
```

#### დასრულებული კოდი

საბოლოოდ თქვენს `models.py`-ს უნდა ჰქონდეს მსგავსი სტრუქტურული სახე. რა საკვირველია, ბაზის მოდელს შეგიძლიათ დაამატოთ ის სასურველი პარამეტრები, რომლის რეგისტრაციის დროს შეტანაც გსურთ მომხმარებლისგან ბაზაში. არ დაგავიწყდეთ რომ ამ პარამეტრების შესაბამისი ფორმა გაამზადოთ რეგისტრაციის გვერდზე გამოსაჩენად.

```python
from myproject import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):

    # Create a table in the db
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
```

### forms.py

ამ თავში ავაწყობთ რეგისტრაციისა და ავტორიზაციის ფორმას. ასევე მოვამზადებთ ფუნქციებს მომხმარებლის მიერ შეყვანილი მონაცემების გადასამოწმებლად. პირველ რიგში შენივიტანოთ საჭირო ბიბლიოთეკები და ხელსაწყოები:

```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from myproject.models import User
```

ჩვენი ამოცანაა შევქმნათ სარეგისტრაციო ფორმების კლასები და გავწეროთ შესავსები ველების ელემენტები:

#### RegistrationForm

```python
class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords Must Match!')])
    pass_confirm = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register!')
```

დააკვირდით რომ ვალიდატორები ფორმას გადაეცემა სიის სახით, იმ შემთხვევაშიც კი თუ ელემენტზე ვიყენებთ მხოლოდ ერთ ვალიდატორს.

რეგისტრაციის ფორმას გავუწერთ ორ ფუნქციონალს, რომელიც ფორმაში შევსებულ მონაცემს გადაამოწმებს. ესენია:

1. უკვე რეგისტრირებულია თუ არა მომხმარებლის სახელი
2. უკვე რეგისტრირებულია თუ არა მომხმარებლის ელექტრონული ფოსტა

##### `validate_email()`

მეთოდის მიზანია ფორმაში შევსებული იმეილი შეადაროს ბაზაში არსებულ ჩანაწერს. იმ შემთხვევაში თუ მონაცემი დაბრუნდება უნდა დავაბრუნოთ ვალიდაციის შეცდომა.

```python
def validate_email(self, email):
    if User.query.filter_by(email=self.email.data).first():
        raise ValidationError('Email has been registered')
```

##### `validate_username()`

```python
def validate_username(self, username):
    if User.query.filter_by(username=self.username.data).first():
        raise ValidationError('Username has been registered')
```

### app.py

დროა დავიწყოთ აპლიკაციის გამართვა და ფუნქციონალის ვიუების აწყობა. ამისთვის შემოვიტანოთ საჭირო ბიბლიოთეკები:

```python
from myproject import app, db
from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_user, login_required, logout_user
from myproject.models import User
from myproject.forms import LoginForm, RegistrationForm
```

`flask_login` -დან შემოტანილ ხელსაწყოებს გამოვიყენებთ როგორც დეკორატორებს შესაბამისი ვიუ ფუნქციებისთვის.

პირველ რიგში გავაკთოთ მთავარი გვერდის მისამართი:

```python
@app.route('/')
def home():
    return render_template('home.html')
```

შემდგომ ავაწყოთ ავტორიზირებული მომხმარებლის მისასალმებელი გვერდი. დანიშნულებიდან გამომდინარე ამ გვერდზე წვდომა მხოლოდ და მხოლოდ ავტორიზებულ მომხმარებელზე უნდა შეიზღუდოს. სწორედ ამ საფეხურზე დაგვჭირდება `login_required` დეკორატორი.

```python
@app.route('/welcome')
@login_required
def welcome_user():
    return render_template('welcome_user.html')
```

ანალოგიურად მოვიქცევით მომხმარებლის ლოგაუთ გვერდის აწყობისას. იმისთვის რომ მომხმარებელმა შეძლოს პლატფორმიდან გამოსვლა, აუცილებელია რომ ის უკვე იყოს ავტორიზებული. შესაბამისად ამ შაბლონსაც მოვათავსებთ `@login_required` დეკორატორში.

მომხმარებლის ლოგაუთ ფუნქციონალზე პასუხს `logout_user()` მეთოდი იღებს. მომხმარებელთან შეტყობინებას გამოვიტანთ `flash alert` -ის დახმარებით:

```python
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('გამოსული ხართ')
    return redirect(url_for('home'))
```

რადგანაც ამ გვერდზე ლოგინ ფორმა გვაქვს გამოვიყენებთ 'GET' და 'POST' მეთოდებზე. პირველ რიგში გამოვიტანოდ გვერდზე ავტორიზაციის ფორმა:

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

```

ჩვენი ამოცანაა ავტორიზაციის ღილაკზე დაკლიკებისას გადავამოწმოთ მომხმარებელი და წარმატებული ავტორიზაციის შემთხვევაში შევუშვათ ის პლატფორმაზე. მომხმარებლის ავტორიზაცია ხდება `login_user()` მეთოდის გამოყენებით, მისთვის მომხმარებლის ობიექტის გადაცემით:

```python

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # ამოვიღოთ მომხმარებელი მონაცემთა ბაზიდან
        user = User.query.filter_by(email=form.email.data).first()

        # შევამოწმოთ რომ მომხმარებელი არსებობს ბაზაში და შეყვანილი პაროლი სწორია

        if user is not None and user.check_password(form.password.data):
            # შევასრულოთ ავტორიზაცია

            login_user(user)
            flash('ავტორიზაცია წარმატებით დასრულდა')

            # თუ მომხმარებელი ცდილობდა რომელიმე გვერდზე შესვლას რომელსაც სჭირდებოდა ავტორიზაცია
            # flask ინახავს მას როგორ 'next' პარამეტრს.
            next = request.args.get('next')

            # შესაბამისად თუ next მნიშვნელობა არსებობს მომხმარებელს გადავიყვანთ ამ მისამართზე
            # წინააღმდეგ შემთხვევაში კი welcome page-ზე.
            if next == None or not next[0] == '/':
                next = url_for('welcome_user')

            return redirect(next)
    return render_template('login.html', form=form)
```

საბოლოოდ დავამატოთ რეგისტრაციის საფეხური:

```python
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('რეგისტრაცია წარმატებით დასრულდა!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)
```

### templates

#### base.html

```html
<!DOCTYPE html>
<html>
  <head>
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
    <meta charset="utf-8" />
    <title></title>
  </head>
  <body>
    <ul class="nav">
      <li class="nav-item">
        <a class="nav-link" href="{{ url_for('home') }}">თავფურცელი</a>
      </li>
      {% if current_user.is_authenticated %}
      <li class="nav-link"><a href="{{ url_for('logout') }}">გამოსვლა</a></li>
      {% else %}
      <li class="nav-link"><a href="{{ url_for('login') }}">შესვლა</a></li>
      <li class="nav-link">
        <a href="{{ url_for('register') }}">რეგისტრაცია</a>
      </li>
      {% endif %}
    </ul>
    {% block content %} {% endblock %}
  </body>
</html>
```

#### home.html

```html
{% extends "base.html" %} {% block content %}
<div class="jumbotron">
  {% if current_user.is_authenticated %}
  <p>გამარჯობა {{ current_user.username }}!</p>
  {% else %}
  <p>გაიარე რეგისტრაცია ან ავტორიზაცია</p>
  {% endif %}
</div>

{% endblock %}
```

#### login.html

```html
{% extends "base.html" %} {% block content %}
<form method="POST">
  {# This hidden_tag is a CSRF security feature. #} {{ form.hidden_tag() }} {{
  form.email.label }} {{ form.email() }} {{ form.password.label }} {{
  form.password() }} {{ form.submit() }}
</form>
{% endblock %}
```

#### register.html

```html
{% extends "base.html" %} {% block content %}
<form method="POST">
  {# This hidden_tag is a CSRF security feature. #} {{ form.hidden_tag() }} {{
  form.email.label }} {{ form.email() }}<br />
  {{ form.username.label }} {{ form.username() }}<br />
  {{ form.password.label }} {{ form.password() }}<br />
  {{ form.pass_confirm.label }} {{ form.pass_confirm() }}<br />
  {{ form.submit() }}
</form>
{% endblock %}
```

#### welcome_user.html

```html
{% extends "base.html" %} {% block content %}
<div class="jumbotron">
  <p>Congrats! You are logged in!</p>
</div>
{% endblock %}
```

## OAuth with Flask

ამ ქვეთავში ვისაუბრებთ OAuth (**O**pen **A**uthorization) ანუ "გარე ავტორიზაციის" ტექნოლოგიაზე. მისი დახმარებით შეგვიძლია გამოვიყენოთ მესამე მხარის სერვისი ავტორიზებისთვის, ისე რომ არ დაგვჭირდეს ისეთი სენსიტიური ინფორმაციის მიმოცვლა, როგორიცაა მომხმარებლის პაროლი. OAuth წარმოადგენს ერთგვარ ავტორიზაციის პროტოკოლს, რომლის დახმარებითაც ერთმანეთისაგან დამოუკიდებელ სერვერებს/სერვისებს შეუძლიათ მომხმარებლის ანგარიშზე წვდომა ერთი ავტორიზაციის ფორმით დართონ.

ხშირ შემთხვევაში შეიძლება დაგვჭირდეს მომხმარებლის გარე სერვისით ავტორიზაცია, მაგალითად facebook, google, github ანგარიშის მეშვეობით, ან საერთოდ არ გვინდოდეს ჩვენს მხარეს ავიღოთ მომხმარებლის ავტორიზაციის პასუხისმგებლობა. საბედნიეროდ უკვე არსებობს უამრავი, საკმაოდ დაცული, უსაფრთხო ავტორიზაციის სერვისი.

ამ შესაძლებლობის ასათვისებლად ჩვენ გამოვიყენებთ Flask-Dance ბიბლიოთეკას. მისი დახმარებით მარტივად ჩავსვავთ გარე სერვისის OAuth ბექენდს ჩვენს აპლიკაციაში.

### [Flask-Dance](https://flask-dance.readthedocs.io/en/latest/)

Flask-Dance ბიბლიოთეკა გვეხმარება OAuthის გამოყენებისას ამ ტექნოლოგიის შიდა მექანიზმის აბსტრაქცირებაში. შეასაბამისად ჩვენ მხოლოდ ფუნქციონალურ ნაწილს ვეხებით და ტექნიკური სირთულეების გადაჭრას ვანდობთ ბიბლიოთეკას. ეს აბსტრაქცია დაშენებულია OAuth2.0 (დღევანდელ სტანდარტ) პროტოკოლზე და Flask-OAuth ბიბლიოთეკაზე რომელიც ფლესკ აპლიკაციაში გარე ავტორიზაციის გამოყენებას უზრუნველყოფს. შესაბამისად Flask-Dance არ არის დამოუკიდებელი ბიბლიოთეკა, არამედ ის დანამატია Flask-ზე რომელიც იყენებს Flask-OAuth ბიბლიოთეკას და ის აერთიანებს სხვადასხვა გარე ავტორიზაციის შესაძლებლობას.

ამასთან მას აქვს საოცრად [მოწესრიგებული დოკუმენტაცია](https://flask-dance.readthedocs.io/en/latest/) როემლშიც აღწერილია თითქმის ყველა თანამედროვე პოპულარული სერვისით ავტორიზაციის პროცესი. [დოკუმენტაციაში აღწერილია ავტორიზების ფუნქციალი როგორც სესიის ისე SQLAlchemy-ს მეშვეობით.](https://flask-dance.readthedocs.io/en/latest/quickstart.html#quickstart)

## Google OAuth

გამოყენების პრინციპი ყველა სერვისზე მეტ-ნაკლებად იდენტურია. ამიტომ მაგალითისთვის გამოვიყენოთ ყველაზე პოპულარული გუგლ ავტორიზაცია.

პროცესის გასამართად დაგვჭირდება რამოდენიმე ცვლადის სისტემაში გაწერა. ეს პროგრამაში გამოსაყენებელი სენსიტიური პარამეტრების შენახვის ერთ-ერთი საუკეთესო გზაა. პროგრამულად გარემოს გამარტვა os მოდულის დახმარებით შეგვიძლია:

```python
import os
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = '1'
os.environ["OAUTHLIB_RELAX_TOKEN_SCOPE"] = '1'
```

გაითვალისწინეთ რომ ეს საფეხური მხოლოდ პროგრამის ლოკალური ტესტირებისას გვჭირდება. სერვერზე გაშვების შემდგომ სისტემის გამართვისას მივხედავთ ამ საკითხს.

#### app.py

```python
from flask import Flask, redirect, url_for, render_template, session
from flask_dance.contrib.google import make_google_blueprint, google

app = Flask(__name__)



app.config['SECRET_KEY'] = 'mysecretkey'


blueprint = make_google_blueprint(
    client_id="######.apps.googleusercontent.com",
    client_secret="####",
    # reprompt_consent=True,
    offline=True,
    scope=["profile", "email"]
)
app.register_blueprint(blueprint, url_prefix="/login")

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/welcome')
def welcome():
    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text
    email=resp.json()["email"]

    return render_template("welcome.html",email=email)

@app.route("/login/google")
def login():
    if not google.authorized:
        return render_template(url_for("google.login"))

    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text
    email=resp.json()["email"]

    return render_template("welcome.html",email=email)


if __name__ == "__main__":
    app.run()
```

#### home.html

```html
<h1>Home Page</h1>
<a href="{{url_for('welcome')}}">Welcome Page Here</a>
<a href="{{url_for('login')}}">Log in with this link.</a>
```

#### welcome.html

```html
<h1>Welcome Google User!</h1>
<h2>Your email is {{email}}</h2>
```
