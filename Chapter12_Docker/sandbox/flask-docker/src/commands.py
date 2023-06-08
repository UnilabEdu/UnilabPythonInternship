from flask.cli import with_appcontext
import click

from src.extensions import db
from src.models import Product, User, Role


def init_db():
    db.drop_all()
    db.create_all()

def populate_db():
    for index in range(10):
        product = Product(name=f"Product {index}", description=f"აღწერა product {index}-ისთვის", price=500 + index)
        product.create(commit=False)
    Product.save()

    roles = ["admin", "moderator", "member"]
    for role in roles:
        new_role = Role(name=role)
        new_role.create()

    admin_user = User(username="admin", password="password123", role_id=1)
    admin_user.create()

@click.command("init_db")
@with_appcontext
def init_db_command():
    click.echo("Creating Database")
    init_db()
    click.echo("Database Created")


@click.command("populate_db")
@with_appcontext
def populate_db_command():
    click.echo("Creating test products")
    populate_db()
    click.echo("Products created")