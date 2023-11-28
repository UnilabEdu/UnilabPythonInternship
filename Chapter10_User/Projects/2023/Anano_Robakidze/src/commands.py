from flask.cli import with_appcontext
import click

from src.extentions import db
from src.models import Product, ProductCategory, User, Role

@click.command("init_db")
@with_appcontext
def init_db():
    click.echo("Database creation in progress")
    db.drop_all()
    db.create_all()
    click.echo("Database created!")


@click.command("populate_db")
@with_appcontext
def populate_db():
    click.echo("Creating categories")
    clothes = ProductCategory(title='Clothes')
    shoes = ProductCategory(title='Shoes')

    clothes.create()
    shoes.create()
    click.echo("Created categories")

    click.echo("Creating products")
    shirt = Product(category_id=clothes.id, title='Shirt', color='red', size='S', price=100, img='19a33af9-dafd-4984-a201-a134b0790205.png')
    shoes = Product(category_id=shoes.id, title='Shoes', color='brown', size='M', price=200, img='c79ee34a-e42f-4ee2-a8fe-e66757965b44.png')

    shirt.create()
    shoes.create()
    click.echo("Created products")

    click.echo("Creating roles")
    userrole = Role(name='User')
    adminrole = Role(name='Admin')
    userrole.create()
    adminrole.create()

    click.echo("Creating test users")
    user1 = User(username="Anano", password="Anano1234", role_id=userrole.id)
    user2 = User(username="adminuser", password="Admin1234", role_id=adminrole.id)
    user1.create()
    user2.create()

    click.echo("Database populated!")