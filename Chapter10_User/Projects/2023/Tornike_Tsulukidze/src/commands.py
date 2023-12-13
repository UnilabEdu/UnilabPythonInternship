from flask.cli import with_appcontext
import click

from src.extensions import db
from src.models import Human, User, Role, Author, Publisher, Category, Book, AuthorBook, PublisherBook, CategoryBook


@click.command("init-db")
@with_appcontext
def init_db():
    click.echo("Creating Database...")
    db.drop_all()
    db.create_all()
    click.echo("Database Created.")


@click.command("populate-db")
@with_appcontext
def populate_db():
    click.echo("Populating database...")

    click.echo("Populating roles...")

    role_user = Role(name="User")
    role_admin = Role(name="Admin")

    role_user.create(commit=False)
    role_admin.create(commit=False)

    click.echo("Populated roles")

    click.echo("Populating users...")

    human_user1 = Human(first_name="tornike", last_name="tsulukidze", birth_year=2005, gender="male")
    human_user2 = Human(first_name="khvicha", last_name="kvaratskhelia", birth_year=2000, gender="male")

    human_user1.create(commit=False)
    human_user2.create(commit=False)

    user1 = User(username="TheMechanicalBeing", email_address="tornike@gmail.com", phone_number="593559933", password="Pass123!", human_id=human_user1.id, role_id=role_admin.id)

    user2 = User(username="NapoliPlayer77", email_address="khvicha@live.com", phone_number="577777777", password="Ilikereal123!", human_id=human_user2.id, role_id=role_user.id)

    user1.create(commit=False)
    user2.create(commit=False)

    click.echo("Populated users.")

    click.echo("Populating authors...")

    human_author1 = Human(first_name="jemal", last_name="kharchkhadze", birth_year=1936, gender="male")
    human_author2 = Human(first_name="charlotte", last_name="brontë", birth_year=1816, gender="female")

    human_author1.create(commit=False)
    human_author2.create(commit=False)

    author1 = Author(human_id=human_author1.id)
    author2 = Author(human_id=human_author2.id)

    author1.create(commit=False)
    author2.create(commit=False)

    click.echo("Populated authors.")

    click.echo("Populating publishers...")

    publisher1 = Publisher(name="პალიტრა L")
    publisher2 = Publisher(name="სულაკაურის გამომცემლობა")

    publisher1.create(commit=False)
    publisher2.create(commit=False)

    click.echo("Populated publishers.")

    click.echo("Populating categories...")

    category1 = Category(name="Romance")
    category2 = Category(name="Bildungsroman")
    category3 = Category(name="Georgian")
    category4 = Category(name="English")

    category1.create(commit=False)
    category2.create(commit=False)
    category3.create(commit=False)
    category4.create(commit=False)

    click.echo("Populated categories.")

    click.echo("Populating books...")

    book1 = Book(title="ქარავანი", publication_year=1984)
    book2 = Book(title="Jane Eyre", publication_year=1847)
    book3 = Book(title="მდგმური", publication_year=1979)

    book1.create(commit=False)
    book2.create(commit=False)
    book3.create(commit=False)

    AuthorBook(book_id=book1.id, author_id=author1.id).create(commit=False)
    AuthorBook(book_id=book2.id, author_id=author2.id).create(commit=False)
    AuthorBook(book_id=book3.id, author_id=author1.id).create(commit=False)

    PublisherBook(book_id=book1.id, publisher_id=publisher2.id).create(commit=False)
    PublisherBook(book_id=book2.id, publisher_id=publisher1.id).create(commit=False)
    PublisherBook(book_id=book3.id, publisher_id=publisher2.id).create(commit=False)

    CategoryBook(book_id=book1.id, category_id=category1.id).create(commit=False)
    CategoryBook(book_id=book1.id, category_id=category2.id).create(commit=False)
    CategoryBook(book_id=book1.id, category_id=category3.id).create(commit=False)

    CategoryBook(book_id=book2.id, category_id=category1.id).create(commit=False)
    CategoryBook(book_id=book2.id, category_id=category2.id).create(commit=False)
    CategoryBook(book_id=book2.id, category_id=category4.id).create(commit=False)

    CategoryBook(book_id=book3.id, category_id=category1.id).create(commit=False)
    CategoryBook(book_id=book3.id, category_id=category3.id).create(commit=False)

    click.echo("Populated books.")

    db.session.commit()

    click.echo("Finished populating database.")
