from flask import redirect, render_template, url_for
from app import app, db
from models import Product, ProductCategory, Actor, ActorFilm, Film, Teacher, Student
from forms import ProductForm


@app.before_first_request
def create_db():
    db.create_all()

    if len(Product.query.all()) == 0:
        # Products
        product_categories = ["CPU", "GPU", "RAM"]
        products = [
            ("Core i7", "CPU", 300),
            ("GTX 4090", "GPU", 1300),
            ("32GB DDR5", "RAM", 400), ]

        for category in product_categories:
            new_category = ProductCategory(name=category)
            db.session.add(new_category)
        db.session.commit()

        category_id = 1
        for product in products:
            new_product = Product(name=product[0], category_id=category_id, price=product[2])
            category_id += 1
            db.session.add(new_product)

        # Teachers and students
        teacher = Teacher(name="Giorgi", age=23)
        students = [{"name": "Joni Jonadze", "email": "Joni@mail.com", 'course': "Python"},
                    {"name": "Mgeli Ramazi", "email": "ramazz@mail.com", 'course': "Python"},
                    {"name": "Chafskvnili Bobi", "email": "bobby@mail.com", 'course': "Python"}]

        db.session.add(teacher)
        db.session.flush()
        for student in students:
            new_student = Student(name=student['name'], email=student['email'], course=student['course'], teacher_id=teacher.id)
            db.session.add(new_student)

        # Actors
        actors = [{"name": "Robert Downey Jr", "age": 57},
                  {"name": "Chris Hemsworth", "age": 41},
                  {"name": "Chris Evans", "age": 39}]

        films = [{"name": "Iron Man 2", "genre": "Action"},
                 {"name": "Thor", "genre": "Action"},
                 {"name": "Avengers", "genre": "Action"},]

        for actor in actors:
            actor = Actor(name=actor['name'], age=actor['age'])
            db.session.add(actor)

        for film in films:
            new_film = Film(name=film['name'], genre=film['genre'])
            db.session.add(new_film)
        db.session.flush()

        actor_films = [{'film_id': 1, 'actor_id': 1},
                       {'film_id': 2, 'actor_id': 2},
                       {'film_id': 3, 'actor_id': 1},
                       {'film_id': 3, 'actor_id': 2},
                       {'film_id': 3, 'actor_id': 3},]

        for actor_film in actor_films:
            new_actorfilm = ActorFilm(film_id=actor_film['film_id'], actor_id=actor_film['actor_id'])
            db.session.add(new_actorfilm)
    db.session.commit()


@app.route("/")
def index():
    return render_template("index.html")


# Product routes
@app.route("/products")
def products():
    products = Product.query.all()
    return render_template("products.html", products=products)


@app.route("/add_product", methods=['GET', 'POST'])
def add_product():
    product_form = ProductForm()
    if product_form.validate_on_submit():
        category = ProductCategory.query.filter_by(name=product_form.product_category.data).first()
        product = Product(name=product_form.product_name.data, price=product_form.price.data, category_id=category.id)
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('products'))
    return render_template("add_product.html", form=product_form)


@app.route("/edit_product/<int:product_id>", methods=['GET', 'POST'])
def edit_product(product_id):
    product = Product.query.get(product_id)
    product_form = ProductForm()

    if product_form.validate_on_submit():
        product.name = product_form.product_name.data
        product.price = product_form.price.data

        category = ProductCategory.query.filter_by(name=product_form.product_category.data).first()
        product.category_id = category.id
        db.session.commit()
        return redirect(url_for('products'))
    return render_template("edit_product.html", product=product, form=product_form)


@app.route("/delete_product/<int:product_id>")
def delete_product(product_id):
    product = Product.query.get(product_id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('products'))


# Teacher
@app.route("/teachers")
def teachers():
    teacher = Teacher.query.get(1)

    # მოდელში გაწერილ db.relationship-ით შეგვიძლია მივწვდეთ ყველა იმ სტუდენტს, სადაც teacher_id ემთხვევა teacher.id-ს
    print(teacher.students)

    students = Student.query.all()
    # ხოლო backref-ში გაწერილი ატრიბუტით, შეგვიძლია პირიქითაც წამოვიღოთ, ანუ student-დან წამოვიღოთ შესაბამისი teacher
    print(students[0].teacher)

    # ამ ატრიბუტებზე წვდომა Jinja-შიც გაქვთ, იხილეთ HTML ფაილი
    return render_template("teacher.html", teacher=teacher, students=students)


# Actors
@app.route("/actors")
def actors():
    actors = Actor.query.all()
    films = Film.query.all()
    return render_template("actors.html", actors=actors, films=films)
