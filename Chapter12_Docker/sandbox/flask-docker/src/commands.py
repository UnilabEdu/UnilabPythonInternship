from flask.cli import with_appcontext
from src.extensions import db
from src.models.product import Product, ProductCategory
from src.models.cinema import Actor, ActorFilm, Film
from src.models.school import Student, Teacher
from src.models.user import User, UserRole, Role
import click


def init_db():
    db.drop_all()
    db.create_all()

def populate_db():
    #Users
    admin_user = User(email="admin@mail.com", username="testuser1", password="password123")
    admin_user.create()

    roles = ["user", "moderator", "admin"]
    for role in roles:
        new_role = Role(name=role)
        new_role.create()

    admin_role = Role.query.filter_by(name="admin").first()
    admin_user_role = UserRole(user_id=admin_user.id, role_id=admin_role.id)
    admin_user_role.create()

    # Products
    product_categories = ["CPU", "GPU", "RAM"]
    products = [
        ("Core i7", "CPU", 300),
        ("GTX 4090", "GPU", 1300),
        ("32GB DDR5", "RAM", 400), ]

    click.echo("Creating product categories")
    for category in product_categories:
        new_category = ProductCategory(name=category)
        db.session.add(new_category)
    db.session.commit()

    category_id = 1
    click.echo("Creating Products")
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

    click.echo("Creating Actors")
    for actor in actors:
        actor = Actor(name=actor['name'], age=actor['age'])
        db.session.add(actor)

    click.echo("Creating Films")
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

@click.command("init_db")
@with_appcontext
def init_db_command():
    click.echo("Creating Database")
    init_db()
    click.echo("Finished Creating Database")


@click.command("populate_db")
@with_appcontext
def populate_db_command():
    populate_db()

