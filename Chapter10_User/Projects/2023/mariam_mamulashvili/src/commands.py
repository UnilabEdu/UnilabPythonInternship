from flask.cli import with_appcontext
import click

from src.models import User, Product, Contact, Works
from src.extensions import db

@click.command("init_db")
@with_appcontext
def init_db():
    click.echo("Database creation in porgress")
    db.drop_all()
    db.create_all()




@click.command("populate_db")
@with_appcontext
def populate_db():
    click.echo("Creating admins")
    user1 = User(username="admin", password="admin123")
    user1.password = "admin123" 
    user2 = User(username="admin2", password="admin456")
    user1.create()
    user2.create()

    click.echo("Creating products")
    media1 = Product(product_name="gimbal", description="gimbal for camera", product_category="image", page_category="gimbal", product_image="https://images-na.ssl-images-amazon.com/images/I/61vU%2B6Tg4KL._AC_SL1500_.jpg")
    media1.create()

    click.echo("Creating works")
    works1 = Works(product_name="Lady of heaven", description="Two stories separated by 1400 years. After losing his mother in the midst of a war-torn country, an Iraqi child, learns the importance and power of patience by discovering the historical story of Lady Fatima and her suffering",
                product_category="Action, Drama, History", product_image="https://sarkestudio.com/wp-content/uploads/elementor/thumbs/597961611747135-p2rwcuqi2o2z8ggbvhgi91b2kcb5fr40wnim38ckts.jpg", release_year="2021", director="Eli King")

    works1.create()








