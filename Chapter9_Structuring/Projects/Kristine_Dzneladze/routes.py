from flask import render_template, flash
from werkzeug.utils import secure_filename
from forms import Registerform
from os import path, getcwd

from app import app, db
from Models import RegisterForm, Book


@app.before_first_request
def create_db():
    db.create_all()
    if len(RegisterForm.query.all()) == 0:
        user = [
            ("Kristine", "Dzneladze", "kristinedzneladze@mail.com",
             "Begginer Writer", "Personal essay", "This is description1", "my file1"),
            ("Anri", "Dzneladze", "Anridzneladze@mail.com",
             "Experienced Writer", "Personal essay", "This is description2", "my file2")
        ]
        for person in user:
            someone = RegisterForm(firstname=person[0], lastname=person[1], email=person[2],
                                   writer_experience=person[3], writer_field=person[4], essay_description=person[5], uploaded_file  = person[6])
            db.session.add(someone)
        db.session.commit()

    if len(Book.query.all()) == 0:

        books = [
            ("Kafka on the Shore", "Haruki Murakami", "Magical realism", "https://www.bookshop.ge/content/uploads/products/9781784877989.jpg"),
            ("The Catcher in the Rye", "J. D. Salinger","Realistic fiction", "https://www.bookshop.ge/content/uploads/products/9780241950425.jpg"),
            ("One Hundred Years of Solitude", "Gabriel García Márquez", "Magic realism", "https://www.bookshop.ge/content/uploads/products/9780141184999.jpg"),
            ("The Shining", "Stephen King", "Horror", "https://www.bookshop.ge/content/uploads/products/9781444720723.jpg"),
            ("Around the World in Eighty Days", "Jules Verne", "Science Fiction", "https://www.bookshop.ge/content/uploads/products/9781509827855.jpg"),
            ("Journey to the Centre of the Earth", "Jules Verne", "Science Fiction", "https://www.bookshop.ge/content/uploads/products/9781509827886.jpg")
        ]

        for item in books:
            book_parametres = Book(bookname = item[0], author = item[1], genre = item[2], img_link = item[3])
            db.session.add(book_parametres)
        db.session.commit()


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/forms", methods=["GET", "POST"])
def forms():
    form = Registerform()
    if form.validate_on_submit():

        user_firstname = form.firstname.data
        user_lastname = form.lastname.data
        user_mail = form.email.data
        user_experience = form.writer_experience.data
        user_writer_field = form.writer_field.data
        user_essay_secription = form.essay_description.data
        filename = secure_filename(form.essay_file.data.filename)
        new_filename = filename.split(".")
        upload_filename = new_filename[0]
        print(upload_filename)


        someone = RegisterForm(firstname=user_firstname, lastname=user_lastname, email=user_mail,
                               writer_experience=user_experience, writer_field=user_writer_field, essay_description=user_essay_secription, uploaded_file = upload_filename)
        db.session.add(someone)
        db.session.commit()

        location = path.realpath(path.join(
            getcwd(), path.dirname(__file__)))
        file_path = path.join(location, "uploaded_files", filename)
        form.essay_file.data.save(file_path)
        flash("Succesfully uploaded")
    else:
        print(form.errors)
    return render_template("forms.html",  register_form=form)


@app.route("/books")
def books():
    all_info  =Book.query.all()
    return render_template("books.html" , book_info = all_info)


@app.route("/youruploadedinfo")
def yourinfo():
    all_data = RegisterForm.query.all()
    return render_template("yourinfo.html", info=all_data)
