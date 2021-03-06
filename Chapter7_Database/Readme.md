# მონაცემთა საცავი

ამ თავში გავივლით შესავალს მონაცემთა ბაზებში პითონის გამოყენებით და ვნახავთ როგორ დავაკავშიროთ ბაზა Flask-ის აპლიკაციასთან.

## შესავალი

ამ ეტაპისთვის უკვე ვიცით თუ როგორ შეგვიძლია მომხმარებლისგან ავიღოთ და დავამუშავოთ მონაცემები. ახლა ჩვენი მიზანია ვისწავლოთ
როგორ შეიძლება მონაცემებს სტრუქტურიზაცია და შენახვა.

Მონაცემთა ბაზა (database) არის ინფორმაციის მოწესრიგებული, დალაგებული კრებული, რომელში შემავალი მონაცემების მართვა, წაკითხვა, ამოღება, დამატება და განახლება გვეხმარება მარტივად გავზარდოთ ჩვენი პროგრამის ფუნქციონალური შესაძლებლობები.

მონაცემთა ბაზა არის საცავი, დახარისხებული ინფორმაციის საწყობი. არსებობს მონაცემთა ბაზის სხვადასხვა ტიპი, თუმცა ჩვენ ორიენტირი გვექნება რელაციურ SQL ტიპის მონაცემთა ბაზაზე.

**Რელაციური მონაცემთა ბაზა** არის მონაცემთა ბაზის ერთ-ერთი ტიპი. Მასში იმფორმაცია ისეა დალაგებული რომ მარტივად შევძლოთ მონაცემის იდენტიფიცირება და მასზე წვდომა, მასში შემავალ მონაცემთან მიმართებაში.
Ხშირ შემთხვევაში, რელაციური ბაზაში, მონაცემები ინახება ცხრილების სახით.

### ცხრილები

ცხრილი არის ერთეული ობიექტი რომელიც ინახავს მონაცემს რელაციურ მონაცემთა საცავში. მონაცემთა საცავი შეიძლება მოიცავდეს ერთ ან მეტ ცხრილს.

ცხრილი კი თავის თავში შედგება სვეტებისა და სტრიქონებისგან (columns/rows). ყოველ სვეტს აქვს განსაზღვრული დასახელება და ინფორმაციის ტიპი
რომელიც მის გასწვრივ სტრიქონებში განთავსდება.

![ცხრილი](https://www.sqlshack.com/wp-content/uploads/2020/07/anatomy-of-a-sql-table-1.png)

სურათზე არის რელაციური SQL ბაზის მარტივი მაგალითი, სადაც ცხრილი **Persons** შედგება **Id**, **Name**, **SurName** და **age** სვეტებისგან. სვეტებში შემავალი ინფორმაცია, განლაგებული მწკრივებად განსხვავდება შიგთავსითა და ტიპით, ზოგიერთი მათგანი ტექსტური, ხოლო ზოგი რიცხვითი სახისაა.

### SQL

**Structured Query Language** ANSI-ის დაყრდნობით ის არის სტანდარტული ენა რელაციურ მონაცემთა ბაზის მართვითი სისტემებისთვის. SQL ბრძანებების მეშვეობით
ხდება მონაცემთა ბაზის განახლება ან ბაზიდან ინფორმაციის ამოღება. ამ ბრძანებებს აქვთ მათთვის განსაზღვრული სინტაქსი. ხშირად გამოყენებადი SQL ბაზებია: PostgreSQL, Oracle, MySQL, SQLite და ა.შ. პითონისა და ფლასკის დაკავშირება საკამოდ იოლია ამ ბაზებთან,
რადგან ისინი უკვე არიან აღჭურვილნი მარტივ გამოყენებადი, ძლიერი იარაღებით, ბაზებთან სამუშაოდ.

Ბაზაში ცხრილის შექმნისთვის საჭირო ძირითადი საფეხურები:

1. ცხრილის დასახელბა
2. ცხრილში შესატანი მონაცემების სვეტებად დაყოფა
3. სვეტების დასახელება
4. სვეტებში მოსათავსებელი მონაცემის ტიპის გაწერა

### სინტაქსის გამოყენების მაგალითი

ცხრილ “users” -ში არსებული ინფორმაციის ვიზუალიზაცია.
ამოღებულია ინსტრუქციით:

```sql
SELECT * FROM users;
```

![select](./images/selectFromSql.png)

_`*` - wildcard, გამოიყენება ერთი ან მეტი სიმბოლოს ჩასანაცვლებლად._

## SQLite

მონაცემთა ბაზასთან ურთიერთობას დავიწყებთ SQLite-ს გამოყენებით.

![sqlite](https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/SQLite370.svg/382px-SQLite370.svg.png)

SQLite არის C-ს ბიბლიოთეკა, რომელიც წარმოადგენს მსუბუქ disk-based მონაცემთა საცავს. ანუ მას არ სჭირდება ცალკე სერვერის პროცესები ფუნქციონირებისთვის.
SQLite ხშირად გამოიყენება პროექტის მოდელირებისთვის, მონაცემის ლოკალური საცავისთვის ან მსუბუქი დატვირთვის ვებ სერვისზე (100,000 მიმოცვლა დღეში).

სიტყვა _lite_ - მსუბუქი, SQLite-ში ამავე მნიშვნელობით გამოიყენება, რადგან SQLite-ის ბზები არის მარტივი ასაწყობი, სამართავი და მოითხოვს მცირე რესურს, რაც შესასრულებელ სამუშაოს ხშირად ამსუბუქებს. ამის გამო SQLite-ს ბაზები გამოიყენება როგორც პროტოტიპირებისას, ასევე დასრულებულ, გაშვებულ პროდუქტში, რომლის საჭიროებებსაც ამგვარი ბაზები აკმაყოფილებენ.

_self-contained, serverless, zero-configuration, transactional._

### მონაცემთა ტიპები

მონაცემთა ბაზები, როგორიც არის MySQL ან PostgreSQL, ძირითად შემთხვევაში იყენებენ მონაცემთა _სტატიკურ ტიპებს_. ეს გულისხმობს, რომ თუ ბაზაში ცხრილის შექმნისას სვეტს მივაკუთნებთ გარკვეულ ტიპს (მაგ. integer, float), მონაცემი რომელიც ამ სვეტის ქვეშ განთავსდება შეზღუდულია მიკუთვნებული ტიპით. შესაბამისად ინტეჯერ ტიპის სვეტში შესაძლებელია მოხვდეს მხოლოდ და მხოლოდ ინტეჯერ ტიპის მონაცემი.

განსხვავებით სხვა ბაზებისგან SQLite იყენებს მონაცემთა _დინამიურ ტიპებს_. რაც გულისხმობს რომ, ნებისმიერ სვეტში შენახული მონაცემის ტიპი განპირობებულია _მხოლოდ და მხოლოდ კონკრეტულად შენახული მონაცემის ტიპით_, და არა სვეტის ტიპით რომლის ქვეშაც მოთავსებულია ეს მონაცემი.

აქედან გამომდინარე, SQLite არ მოითხოვს სვეტის შექმნისას, მასში მოსათავსებელი მონაცემის ტიპის წინასწარ გაწერას და აქედან გამომდინარე, წინასწარ გაწერილი მონაცემის ტიპის სვეტში შესაძლებელია განსხვავებული ტიპის მონაცემის შენახვაც.

SQLite გვთავაზობს 5 პირობით მონაცემთა ტიპს, რომელსაც _მეხსიერებათა კლასებს_ უწოდებენ - storage classes

![SQLITE მეხსიერებათა კლასები](https://docplayer.net/docs-images/63/49185735/images/11-2.jpg)

## Python და SQLite

პითონთან სამუშაოდ გამოვიყენებთ Gerhard Häring-ის მიერ შექმნილ მოდულს sqlite3.
მოდულის გამოსაყენებლად უნდა შევქმნათ დამაკავშირებელი ობიექტი connection, რომელიც წარმოადგენს sqlite მონაცემთა ბაზას. ამისთვის უნდა შემოვიტანოთ sqlite3-ის მოდელი და შესაბამის მაკავშირებელს ობიექტს უნდა გადავცეთ ბაზის მონაცემი, ჩვენს შემთხვევაში დასახელება.

```python
import sqlite3
conn = sqlite3.connect('mydata.db')
```

ამრიგად პროგრამის გაშვების ადგილას შეიქმნება ახალი ფაილი mydata.db, რომელიც უკვე მზად არის გამოსაყენებლად დამატებითი საფეხურების გარეშე.

მას შემდეგ რაც შევქმნით მაკავშირებელ ობიექტს conn, ჩვენ შეგვიძლია მისგან ავიღოთ კურსორის ობიექტი, რომლის `execute() ` მეთოდის გამოყენებითაც შევძლებთ მონაცემთა ბაზაზე SQL ბრძანებების შესრულებას, მეთოდისთვის შესაბამისი პარამეტრების გადაცემით.

პროგრამულად ბაზაში ახალი ცხრილის და მასში მონაცემის დამატების პროცესი ასე გამოიყურება:

```python
# ვქმნით კურსორს
cursor = conn.cursor()

# ვქმნით ცხრილს
cursor.execute('''CREATE TABLE წიგნები
             (თარიღი text, ავტორი text, დასახელება text, ტირაჟი real, ფასი real)''')

# ვამატებთ წიგნს როგორც მონაცემს
cursor.execute("INSERT INTO წიგნები VALUES ('2017-04-27','დათო სამნიაშვილი','MOX (მოქსი)',100,9.50)")

# ვინახავთ (commit) ცვლილებებს
conn.commit()

# პროცესის დასრულების შემდგომ ვხურავთ კავშირს
conn.close()
```

გაითვალისწინეთ, ისეთ შემთხვევაში სადაც ბრძანება ბაზაში მონაცემის ჩაწერას, ან შეცვლას მოითხოვს აუცილებელია commit() მეთოდის გამოყენება, წინააღმდეგ შემთხვევაში, პროცედურის დასრულების შემდგომ ბაზაზე შესრულებული ცვლილება არ აისახება.

### პარამეტრების გადაცემა

შესასრული სამუშაოების ავტომატიზაციისათვის, წინასწარ უნდა გავამზადოთ ბაზასთან გადასაცემი ბრძანებების შაბლონები. ამ ბრძანებებს შეგვიძლია გავატანოთ ცვლადებში შენახული პარამეტრები. პარამეტრების შაბლონურ სტრინგში ჩასმა შესაძლებელია სტრინგ ფორმატინგით, თუმცა ეს არც ისე უსაფრთხო და არარეკომენდირებული მეთოდია.

```python
# არ გამოიყენოთ მსგავსი მეთოდ -- არ არის სანდო!
parameters = 'MOX (მოქსი)'
cursor.execute("SELECT * FROM წიგნები WHERE დასახელება = '%s'" % parameters)
```

ამის მაგივრად execute() მეთოდს, SQL ინსტრუქციასთან ერთად უნდა გადავცეთ შესაბამის ცვლადში მოთავსებული პარამეტრები, SQL ინსტრუქციაში კი ცვლადის ადგილას მივუთითებთ "?" ნიშნით. ცვლადის ტიპი რომელსაც შემსრულებელ მეთოდს გადავცემთ, მიუხედავად იმისა ერთი თუ რამოდენიმე წევრისაგან შედგება ეს პარამეტრი უნდა იყოს tuple. მაგალითად parameters = ('დათო სამნიაშვილი',)

```python
# ერთი პარამეტრის შემთხვევაში
parameters = ('MOX (მოქსი)',)
cursor.execute('SELECT * FROM წიგნები WHERE დასახელება=?', parameters)

# რამოდენიმე პარამეტრის შემთხვევაში
parameters = ('MOX (მოქსი)','დათო სამნიაშვილი')
cursor.execute('SELECT * FROM წიგნები WHERE დასახელება=?, ავტორი=?', parameters)
```

ამავდროულად, ერთი მეთოდით executemany() შეგვიძლია რამოდენიმე მონაცემის ერთდროულად შეტანა/დამუშავება. მაგალითად:

```python
books = [('2017-01-27','ზურა ჯიშკარიანი','საღეჭი განთიადები: უშაქროდ',1000,9.50),
         ('2017-04-27','დათო სამნიაშვილი','MOX (მოქსი)',1000,9.50),
         ('1875-04-06', 'ჟიულ ვერნი', 'საიდუმლო კუნძული', 1000,9.50),
        ]
cursor.executemany('INSERT INTO წიგნები VALUES (?,?,?,?,?)', books)
```

--- ჩაამატე fetchall, fetchone ---

ბაზაში მონაცემის განახლებისთვის ვიყენებთ შემდეგი ტიპის ინსტრუქციას:

```sqlite
UPDATE წიგნები SET დასახელება=? WHERE ავტორი=?
```

წასაშლელად:

```sqlite
"DELETE FROM წიგნები WHERE დასახელება=?"
```

## Flask და მონაცემთა ბაზა

იმისთვის რომ Flask აპლიკაციაში მონაცემთა ბაზის ჩაშენება შევძლოთ დაგვჭირდება 3 ძირითადი საფეხურის გავლა:

1. Flask-ის კონფიგურირება მონაცემთა ბაზისთვის
2. ბაზის მოდელის აწყობა ფლასკში
3. ბაზის მოდელზე ვებ რესურსის მორგება

### მაგალითი

```python
import os #გამოვიყენებთ რესურსების მისამართებთან სამუშაოდ
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class NameModel(db.Model):
    # დეფოლტ მნიშვნელობად ცხრილს დაერქმევა კლასის სახელი.
    # __tablename__ = "name_of_table" # მოხსენი კომენტარი თუ გინდა რაიმე განსხვავებულის დარქმევა ცხრილისთვის და გადაეცი სტრინგად

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)

    def __init__(self, username, email):
        self.email = email
        self.username = username

    def __repr__(self):
        return f'email of {username} is {email}'

```

### flask აპლიკაციის გამართვა

დავიწყოთ მუშაობა [**Flask-SQLAlchemy**](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/) -ში.

Flask-SQLAlchemy არის Flask-ის დამატებითი ბიბლიოთეკა, რომელიც ჩვენს პროექტს დააშენებს SQLAlchemy-ს შესაძლებლობებს.
მონაცემთა ბაზასთან სამუშაოდ საკმარისია flask-ის აპლიკაციის კონფიგურაციაში მონაცემთა ბაზის მისამართის მითითება და ამ აპლიკაციით SQLAlchemy ობიექტის შექმნა.

დასაწყებად დავაყენოთ ბიბლიოთეკა:

```python
pip install -U Flask-SQLAlchemy
```

![FlaskAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/_images/flask-sqlalchemy-title.png)

იმისთვის რომ შევძლოთ ჩვენს სერვისში ბაზის გამოყენება, უნდა შევქმნათ flask აპლიკაცია შესაბამისი კონფიგურაციით. ამისთვის რამოდენიმე მარტივი ნაბიჯის გავლა დაგვჭირდება:

1. შევქმნათ Flask app
2. დავამატოთ აპლიკაციას SQLAlchemy-ს კონფიგურაცია
3. გადავცეთ ჩვენი აპლიკაცია SQLAlchemy-ს კლასის გამოძახებისას.

პითონის კოდში შექმნილი ბაზის მოდელი აღწერს როგორი იქნება რეალური ცხრილი მონაცემთა ბაზაში.
შესაბამისად კოდიდან შევძლებთ ავტომატურად ცხრილის შექმნას, ამ ცხრილის შესაბამისი ბაზის მოდელის გაწერით, პითონი კი მუშაობისას ავტომატურად დააგენერირებს ბაზაში შესაბამის ცხრილებს.

ამიტომ წარმოიდგინეთ ფლასკ აპლიკაციაში მოდელის ხსენებისას რომ რეალურად ვგულისხმობთ ცხრილს რომელიც ამ მოდელის უკან დგას.
როგორც ვახსნეთ მოდელის აწყობა ხდება კოდში შესაბამისი კლასის გაწერით. ამ კლასს მოდელის შესაძლებლობებს ფლასკის ბიბლიოთეკიდან ამოღებული Model-ის მემკვიდრეობა აძლევს.

#### გავმართოთ აპლიკაცია

აპლიკაციის გასამართად შემეგი რესურსების დაგვჭირდება:

```python
import os #გამოვიყენებთ რესურსების მისამართებთან სამუშაოდ
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
```

ბაზის დირექტორიის მისამართის ამოსაღებად გამოვიყენებთ os ბიბლიოთეკას.

```python
basedir = os.path.abspath(os.path.dirname(__file__))
```

როდესაც პითონში იტვირთება რაიმე მოდელი, პითონში ჩაშენებული `__file__` იღებს ფაილის დასახელების მნიშვნელობას.
`os.path.dirname(__file__)` გვაძლევს ინფორმაციას დირექტორიაზე რომელშიც ეს ფაილია მოთავსებული.
`os.path.abspath()` კი გვაძლევს სრულ მისამართს რომელიც პროგრამის ფაილს გააჩნია.

შევქმნათ აპლიკაციის ობიექტი რომელსაც ბაზასთან დავაკავშირებთ:

```python
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
```

db-ში მოთავსებულია ამ აპლიკაციის ბაზის ობიექტი, რომელშიც არის ჩვენს აპლიკაციაში გამოყენებადი ყველა ხელსაწყო რასაც SQLAlchemy გვთავაზობს.

ერთ-ერთი მათგანია Model. მისი დახმარებით შევძლებთ ავაწყოთ ბაზის მოდელი და შევძლოთ პითონის კოდიდან ბაზის მართვა.

### [ბაზის მოდელის აწყობა](https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#simple-example)

1. შექმენი მოდელის კლასი
2. მემკვიდრეობა db.Model -ისგან
3. სურვილისამებრ გადაეცით ცხრილის სახელი
4. კლასს ატრიბუტებად დაურთეთ ცხრილის სვეტები (დასახელება, აღწერა)
5. ჩაამატეთ `__init__` და `__repr__` მეთოდები

შესაბამისად შევქმნათ მოდელის კლასი, და გადავცეთ მემკვიდრეობით წინა საფეხურში შექმნილი ბაზის მოდელის თვისებები.

```python
class NameModel(db.Model):
    # დეფოლტ მნიშვნელობად ცხრილს დაერქმევა კლასის სახელი.
    # __tablename__ = "name_of_table" # მოხსენი კომენტარი თუ გინდა რაიმე განსხვავებულის დარქმევა ცხრილისთვის და გადაეცი სტრინგად

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
```

სვეტების არწერა მოდელში ხდება კლასის ატრიბუტებად. ცხრილში თითოეული სვეტი შეესაბამება მოდელში გაწერილ თითოეულ ბაზის ატრიბუტს.
როგორც შევთანხმდით ბაზის ცხრილის სვეტის აღწერისას გვჭირდება მასში შემავალი მონაცემთა ტიპის გაწერა. SQLAlchemy-ს შემოთავაზებული ძირითადი მონაცემთა ტიპები:

| ტიპი         | აღწერა                                                                             |
| ------------ | ---------------------------------------------------------------------------------- |
| Integer      | მთელი რიცხვები                                                                     |
| String(size) | ტექსტი მაქსიმალური ზომის ლიმიტით (ზოგი ტიპის ბაზებთან სამუშაოდ არ არის აუცილებელი) |
| Text         | დიდი ზომის ტექსტი                                                                  |
| DateTime     | თარიღი აღებული datetime ობიექტიდან.                                                |
| Float        | წილადი                                                                             |
| Boolean      | ბულიანი (ჭეშმარიტი/მცდარი)                                                         |

ამის შემდეგ აუცილებელია init მეთოდის გაწერა, რომ შევძლოთ ამ ბაზის მოდელის ობიექტის შექმნა კოდში გამოსაყენებლად.

```python
    def __init__(self, username, email):
        self.email = email
        self.username = username
```

ამრიგად მოდელის ატრიბუტები მიიღებენ იმ მნიშვნელობას რომელსაც მათ ობიექტის შექმნისას მივანიჭებთ. მოდელის სტრინგ რეპრეზენტაცია შემდეგნაირად შეგვიძლია გავწეროთ:

```python
    def __repr__(self):
        return f'email of {username} is {email}'
```

### ბაზის გამართვა

შევქმნათ ახალი პითონის ფაილი `setupdatabase.py` სადაც შემოვიტანთ ბაზას `db` და მოდელს.

```python
from basic import db, NameModel
```

შევქმნათ ფუნქციონალი რომელიც ავტომატურად შექმნის ბაზას და მოათავსებს მასში ცხრილებს ბაზის მოდელის მიხედვით `create_all()` მეთოდის გამოყენებით.

```python
db.create_all()
```

ამის შემდეგ შესაძლებლობა გვაქვს შევქმნათ ობიექტები ბაზის მოდელის მიხედვით და დავამატოთ ისინი ბაზაში:

```python
# შევქმნათ ბაზის ახალი წევრები
user1 = NameModel('username1','user1@mail.com')
user2 = NameModel('username2','user2@mail.com')

# შევამოწმოთ თითოეული მომხმარებლის id ბაზაში
print(user1.id)
print(user2.id)

# დავამატოთ მონაცემები ბაზაში
db.session.add_all([user1,user2])

# ან ინდივიდუალური დამატებისას
# db.session.add(user1)
# db.session.add(user2)

# და ავსახოთ ცვლილებები ბაზაზე
db.session.commit()

# შევამოწმოთ id თავიდან
print(user1.id)
print(user2.id)
```

`db.session.add(დასამატებელი_ობიექტი)` ან `db.session.add_all([დასამატებელი,ობეიქტების,სია])` გვაძლევს შესაძლებლობას სამუშაო სესიაში შენახული ობიექტი/ები დავამატოთ ბაზაში და
შემდგომ ავსახოთ სესიაში შეტანილი ცვლილებები `db.session.commit()` მეთოდის გამოყენებით.

## CRUD

Create, Read, Update, Delete

### Create

ბაზაზე მოთხოვნილი ყველა ცვლილება, იქნება ეს მონაცემის დამატება თუ განახლება ინახება სესიაში მის შესრულებამდე.

შესაბამისად მონაცემის დამატების პროცესი 3 მთავარ საფეხურად იყოფა:

1. ბაზის ობიექტის შექმნა - `user1 = NameModel('username1','user1@mail.com')`
2. ობიექტის სესიაში დამატება - `db.session.add(user1)`
3. სესიის ბაზაზე ასახვა - `db.session.commit()`

### Read

როგორ ამოვიღოთ დამატებული ინფორმაცია ბაზიდან ? ამ ამოცანის შესასრულებლად Flask_SQLAlchemy ბაზის მოდელს ანიჭებს `query` ატრიბუტს. როდესაც ვაკითხავთ ამ ატრიბუტს, ის გვიბრუნებს ახალ ობიექტს ბაზიდან აღებული ინფორმაციით. ამ ობიექტზე შეგვიძლია შემდგომ ისეთი მეთოდების გამოყენება
როგორიც არის `filter()` ინფორმაციის გასაფილტრად და შემდგომ ავირჩიოთ მონაცემი `all()` ან `first()` -ის გამოყენებით.

მაგალითად:

```python
users = NameModel.query.all() # მიიღებს ბაზის მოდელით შენახული ყველა წევრის მნიშვნელობას

# ID-ით ამორჩევა
user_by_id = NameModel.query.get(2) # get() გადავცემთ id-ს ინდექსს

# ფილტრები

user2 = NameModel.query.filter_by(username = 'user2').first() # first() დააბრუნებს ობიექტის მხოლოდ პირველ ელემენტს.
```

### Update

მონაცემის განახლება მონაცემის დამატების მსგავსად ხდება ბაზის მოდელის გამოყენებით. პირველ რიგში ბაზაში არსებული მონაცემით უნდა შევქმნათ ობიექტი,
როგორც ეს read თავში გვაქვს განხილული, შემდგომ ვცვლით სასურველ პარამეტრს და ვამატებთ ცვლილებას სესიის გამოყენებით.

განვიხილოთ მაგალითი სადაც გვინდა მეორე მომხმარებელს შევუცვალოთ მეილის მისამართი. ამისთვის:

```python
user2 = NameModel.query.filter_by(username = 'user2').first() #ამოვიღოთ მომხმარებლის ობიექტი ბაზიდან
user2.email = "new_mail@mail.com" # ვცვლით სასურველ პარამეტრს
db.session.add(user2) # ვამატებთ ობიექტს ბაზის სესიაში
db.session.commit() # საბოლოოდ გადაგვაქვს ცვლილებები ბაზაში
```

### Delete

განახლების მსგავსად გვჭირდება შევქმნათ ობიექტის ბაზაში არსებული მონაცემისგან ხოლო შემდგომ წავშალოთ იგი.

```python
user_by_id = NameModel.query.get(1) # ამოვიღეთ id-ით მეორე ობიექტი ბაზიდან
db.session.delete(user_by_id) # წავშალე ობიექტი სესიიდან
db.session.commit # გადავიტანე სასეიაში შეტანილი ცვლილებები ბაზაში
```

## [Flask Migrate](https://flask-migrate.readthedocs.io/en/latest/)

### მიმოხილვა

ბაზის მოდელის შემდგომ მუშაობისას არის შემთხვევები როდესაც გვჭირდება მოდელში ცვლილებების შეტანა, მაგალითად ახალი სვეტის დამატება.

ამ ცვლილებების შეტანისას საჭიროა ცვლილებების მიგრაცია რომ შევძლოთ მისი ასახვა მონაცემთა ბაზაზე.

პირველ რიგში დავაყენოთ ბიბლიოთეკა:

```python
pip install Flask-Migrate
```

Flask Migrate-ს გამოყენება შესაძლებელია, როგორც პროგრამულად - პითონის კოდში, ასევე ტერმინალიდან. ის გვაძლევს შესაძლებლობას შევიტანოთ ცვლილებები ბაზის მოდელში და მასში შეტანილი ცვლილებები გადავიტანოთ ბაზაზე.

ხელსაწყოს გააჩნია 4 ძირითადი ბრძანება რომელზეც ვიმუშავებთ.

მნიშვნელოვანი საფეხურია გავამზადოთ environmental variables - სამუშაო გარემოს უნდა მივუთითოთ ფლასკის აპლიკაციაზე. ამისთვის ტერმინალი უნდა მივიყვანოთ სამუშაო დირექტორიაზე (`cd <directory_path>`) და გავუშვათ ბრძანება:

- MacOS/Linux: `export FLASK_APP=app.py`
- Windows: `set FLASK_APP=app.py`

_თუ არ იქნებით სამუშაო დირექტორიაში ტერმინალში გამოიტანს შეცდომას._

| ბრძანება                             | აღწერა                          |
| ------------------------------------ | ------------------------------- |
| `flask db init`                      | სამიგრაციო დირექტორიის გამართვა |
| `flask db migrate -m "შეტყობინება" ` | სამიგრაციო ფაილის გამართვა      |
| `flask db upgrade`                   | ბაზის განახლება მიგრაციიდან     |

ამ ბრძანებების გამოყენება რომ შევძლოთ, ჩვენს აპლიკაციას უნდა დავუმატოთ მიგრაციის უნარი.

### აპლიკაციის გამართვა

პროგრამაში მიგრაციის შესაძლებლობების შემოსატანად აპლიკაციაში დაგვჭირდება რამოდენიმე ხაზის დამატება.

პირველ რიგში აუცილებელია ბიბლიოთეკის შემოტანა:

```python
from flask_migrate import Migrate
```

ამის შემდეგ აუცილებელია დავაკავშიროთ ფლასკის აპლიკაციის ობიექტთან მონაცემთა ბაზის ობიექტის დახმარებით.

```python
Migrate(app, db)
```

აპლიკაცია მზადაა მიგრაციისთვის, შესაბამისად შეგვიძლია ბაზის მოდელში შევიტანოთ ცვლილებები. მაგალითად დავამატოთ ახალი სვეტი.

### ბრძანებების მიმდევრობა

ამრიგად აპლიკაცია მზად არის მიგრაციის ბრძანებების გასაშვებად:

> `flask db init`
>
> `flask db migrate -m "created new column"`
>
> `flask db upgrade`

## მოდელის გამზადება რესურსისათვის

ამ ეტაპამდე გავეცანით თუ როგორ შეგვიძლია შევქმნათ ბაზის მოდელი და ამ მოდელის მიხედვით აწყობილ ბაზის ობიექტზე ჩავატაროთ CRUD ოპერაციები.
ამ ქვეთავში გავაკეთებთ კოდის ოპტიმიზაციას და საბოლოოდ გავმართავთ ბაზის მოდელს Flask რესურსთან სამუშაოდ. გამართულ მოდელს შემდეგ თავში დავაკავშირებთ Flask-ის რესურსთან **Flask-RESTful** -ის გამოყენებით.

### მოდელში CRUD მეთოდების დამატება

შევქმნათ სავარჯიშო ბაზის მოდელი და დავამატოთ მასში CRUD მეთოდის ასაწყობი შაბლონი.

```python
from app import db


class UserModel(db.Model):
    __tablename__ = 'collection'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def create(self):
        pass

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
```

​

#### 1. **Create** - მონაცემის დამატება

შეთანხმებისამებრ, მონაცემის ბაზაში დასამატებლად, მონაცემის მატარებელი ობიექტი უნდა დაემატოს სესიაში და აისახოს ბაზაზე.

წარმოვიდგინოთ რომ უკვე გვაქვს ბაზის მოდელის მიხედვით შექმნილი ობიექტი. მაგალითად:

```python
user = UserModel("ემეტ", "ბრაუნი")
```

რადგან ამ საფეხურზე ობიექტი `create` მეთოდს გადაეცემა `self` -ის, ანუ "თავისი თავის" მეშვეობით, ჩვენ შეგვიძლია `self` დავამატოთ სესიას და გადავიტანოთ ცვლილებები ბაზაში. შესაბამისად კოდს ექნება შემდეგი სახე:

```python
def create(self):
    db.session.add(self)
    db.session.commit()
```

#### 2. **Read** - მონაცემის ამოღება

რადგან მონაცემი რომლითაც ობიექტი უნდა შეიქმნას ბაზიდან ამოგვაქვს, ხოლო ეს ფუნქციონალი კლასის მეთოდებში გვინდა გავწეროთ დაგვჭირდება გამოვიყენოთ კლას მეთოდი.

როგორც CRUD ფუნქციონალის გარჩევისას ვნახეთ, მონაცემის წაკითხვისას ვიყენებთ ბაზის მოდელის კლასის ატრიბუტს `query`-ს. მას შეგვიძლია ფუნქციონალიდან გამომიდნარე დავამატოთ მეთოდები ( `all()`, `first()` ... ), სასურველი მონაცემის ამოსაღებად.

მაგალითისთვის:

```python
    @classmethod
    def read(cls):
        '''მეთოდი აბრუნებს ცხრილის პირველ ჩანაწერით შექმნილ ბაზის ობიექტს'''
        return cls.query.first()
```

`UserModel.read()` მეთოდის კონსტრუქტორად გამოყენებით ჩვენ უკან დაგვიბრუნდება ბაზიდან ამოღებული ინფორმაციით განაყოფიერებული ატრიბუტების მქონდე ობიექტი.

#### 3. **Update** - მონაცემის განახლება

რადგან მონაცემის შექმნაც და განახლებაც `db.session.add()` მეთოდის გამოყენებით ხდება **1. Create - მონაცემის დამატება**-ში შექმნილ მეთოდს გადავარქვათ სახელი `create` და დავარქვათ მეთოდს `save_to_db()`. ამ მეთოდს გამოვიყენებთ როგორც მონაცემის ჩასაწერად ასევე მონაცემის გასანახლებლად.

```python
def save_to_db(self):
    '''მეთოდი ინახავს ობიექტს ბაზაში'''
    db.session.add(self)
    db.session.commit()
```

განახლებისთვის დაგვჭირდება ბაზიდან ამოღებული ობიექტისთვის სასურველი ატრიბუტის მნიშვნელობის შეცვლა, შემდგომ კი ამ ობიექტზე `save_to_db()` მეთოდის გამოძახება.

#### 4. **Delete** - მონაცემის ამოშლა

`delete`-ს მაგივრად დავარქვათ მეთოდს `delete_from_db()` რადაგან გამოვკვეთოთ რომ ის `save_to_db()`-ის საპირისპირო მეთოდია

```python
def delete_from_db(self):
    '''მეთოდი შლის ობიექტს ბაზიდან'''
    db.session.delete(self)
    db.session.commit()
```

მონაცემის წასაშლელად დაგვჭირდება ბაზიდან სასურველი ობიექტის ამოღება, შემდგომ კი ამ ობიექტზე `.delete_from_db()` მეთოდის გამოყენება.

ამრიგად ჩვენი მოდელი თითქმის მზად არის Flask აპლიკაციასთან სრული ფუნქციური კავშირისათვის. მომდევნო თავში მოდელს დავამატებთ სერვისის შესაბამის საბოლოო შტრიხებს და დავაერთებთ Flask აპლიკაციის რესურსთან. რესურსის შესაქმნელად კი გამოვიყენებთ Flask-RESTful -ს. გავეცნობით REST API -ს და მისი Flask-RESTful -ით გამართვის პრინციპებს.

## [classmethod](https://www.programiz.com/python-programming/methods/built-in/classmethod)

_`classmethod(function)` პითონის ჩაშენებული ფუნქციონალია რომელიც გადაცემული ფუნქციის კლას მეთოდს აბრუნებს._

ხშირად კლას მეთოდი გამოიყენება დეკორატორის სახით და ის გარს აკრავს ფუნქციას რომლის კლას მეთოდის ამოღებაც გვსურს. მაგალითად:

```python
@classmethod
def func(cls, args...)
```

შესაბამისად ფუნქცია პირველ არგუმენტად იღებს cls პარამეტრი ანუ კლასი რომლის კლასმეთოდსაც ეკუთვნის ფუნქცია.

### რა არის კლას მეთოდი?

კლას მეთოდი არის ისეთი მეთოდი რომელიც მუშაობს უშუალოდ კლასზე და არა მის ობიექტზე. შესაბამისად ის არ საჭიროებს კლასის ობიექტის შექმნას, ისე როგორც [staticmethod](https://www.programiz.com/python-programming/methods/built-in/staticmethod).

კლას მეთოდი მუშაობს უშუალოდ კლასზე და მისი გამოყენება შეგვიძლია უშუალოდ კლასიდან ობიექტის კონსტრუქტორად, რადგან მისი გამოძახება შეგვიძლია როგორც კლასიდან ისე მისი ობიექტიდან:

```python
Class.classmethod()
Or even
class_object.classmethod()
```

მაგრამ ორივე შემთხვევაში ის პირველ არგუმენტად აუცილებლად იღებს თვითონ კლასს `cls`.

```python
def classMethod(cls, args...)
```

### როგორ გამოვიყენოთ კლას მეთოდი კონსტრუქტორად?

როგორც ვახსენეთ კლას მეთოდის გამოძახებით შეგვიძლია უკან დავაბრუნოთ ამ კლასის ტიპის ობიექტი.

```python
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def name_splitter(cls, name):
        first_name, last_name = name.split()
        return cls(first_name, last_name)

    def display(self):
        print(f'First Name: {self.first_name} \n Last Name: {self.last_name}')


person = Person.name_splitter('Emmet Brown')
person.display()
```

**Output**

```
First Name: Emmet
Last Name: Brown
```

`name_splitter` შუაზე ყოფს `Person.name_splitter('Emmet Brown')` -ით გადაცემულ სტრინგს და ამ მონაცემებით ქმნის Person კლას ტიპის ობიექტს. რადგან კლასი კლას მეთოდს გადაეცემა როგორც cls, ახალ ობიექტს ვქმნით მისთვის პარამეტრების გადაცემით: `cls(first_name, last_name)`.

ამ მეთოდით შექმნილს ობიექტს კი საბოლოოდ `return` ბრძანებით ვაბრუნებთ უკან და ვინახავთ `person` ცვლადში. შესაბამისად `person`-ზე შეგვიძლია `Person`-ში გაწერილი მეთოდების გამოყენება.

## Relationship

> model.py

```python
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    # One to many
    book = db.relationship('Books', backref="student", lazy='dynamic')
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

    def show_books(self):
        for book in self.book:
            print(book.name)


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Connect the teacher to the Student that "owns" it.
    # We use student.id because __tablename__='student'
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    name = db.Column(db.String)

    def __init__(self, name, student_id):
        self.student_id = student_id
        self.name = name


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    name = db.Column(db.String)

    def __init__(self, name, student_id):
        self.student_id = student_id
        self.name = name

```

> populate.py

```python
# This script will create some students, Teachers, and Bookss!
# Note, if you run this more than once, you'll be creating dogs with the same
# name and duplicate Teachers. The script will still work, but you'll see some
from model import db, Teacher, Student, Books

# Create 2 students
rufus = Student("Rufus")
fido = Student("Fido")

# Add students to database
db.session.add_all([rufus,fido])
db.session.commit()

# Check with a query, this prints out all the students!
print(Student.query.all())

# Grab Rufus from database
# Grab all students with the name "Rufus", returns a list, so index [0]
# Alternative is to use .first() instead of .all()[0]
rufus = Student.query.filter_by(name='Rufus').all()[0]

# Create an Teacher to Rufus
jose = Teacher("Jose", rufus.id)

# Give some Bookss to Rufus
Books1 = Books('Chew Books',rufus.id)
Books2 = Books("rufu's fav book",rufus.id)

# Commit these changes to the database
db.session.add_all([jose,Books1,Books2])
db.session.commit()

# Let's now grab rufus again after these additions
rufus = Student.query.filter_by(name='Rufus').first()
print(rufus)

# Show Bookss
print(rufus.show_books())

# You can also delete things from the database:
# find_student = Student.query.get(1)
# db.session.delete(student)
# db.session.commit()

```
