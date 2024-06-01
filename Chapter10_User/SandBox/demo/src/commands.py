from flask.cli import with_appcontext
import click

from src.ext import db
from src.models import Product, User

@click.command("init_db")
@with_appcontext
def init_db():
    click.echo("Creating Database")
    db.drop_all()
    db.create_all()
    click.echo("Database Created")


@click.command("populate_db")
@with_appcontext
def populate_db():
    click.echo("Creating test products")
    for index in range(10):
        product = Product(name=f"Product {index}", description=f"აღწერა product {index}-ისთვის", price=500 + index)
        product.create(commit=False)
    Product.save()

    click.echo("Creating admin user")
    admin = User(username="admin", password="AdminPass123", role="Admin")
    admin.create()

    normal = User(username="user", password="password", role="Member")
    normal.create()
    click.echo("DB created")