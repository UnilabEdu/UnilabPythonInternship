from market.extensions import db
from flask.cli import with_appcontext
import click
from market.models import Product, User, Role
from market.scrapdata import scrapped_data


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
    click.echo("Creating Test Product")

    roles = ['admin', 'member']
    for role in roles:
        new_role = Role(name=role)
        new_role.create()

    admin_user = User(username='admin', password='admin123', email='admin@gmail.com', role_id=1)
    admin_user.create()
    datas = scrapped_data()
    for data in datas:
        product = Product(part=data['part_name'],
                          name=data['name'],
                          description=data['about'],
                          price=data['price'],
                          image=data['image'],
                          owner_id=admin_user.id)
        product.create(commit=False)
    Product.save()

    click.echo("Products Created")
