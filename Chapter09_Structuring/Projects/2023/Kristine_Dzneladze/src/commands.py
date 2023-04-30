from flask.cli import with_appcontext
import click
from src.extensions import db
from src.data import books 
from src.models.books import Book 

@click.command("init_db")
@with_appcontext
def init_db():
    click.echo("Creating db")
    db.drop_all()
    db.create_all()
    click.echo("Finished Creating db")


@click.command("populate_db")
@with_appcontext
def populate_db():
    click.echo("populating db")
    for item in books:
        book_parametres = Book(bookname = item[0], author = item[1], genre = item[2], img_link = item[3])
        book_parametres.create()
    book_parametres.save()
    click.echo("Finished populating db")


