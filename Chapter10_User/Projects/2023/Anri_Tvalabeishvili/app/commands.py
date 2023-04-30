from flask.cli import with_appcontext
from app.extensions import db
from app.models.product import Game, Gift
from app.models.user import User
import click


from data import Admins, Games, Gifts




@click.command("init_db")
@with_appcontext
def init_db():
    click.echo("Creating Database")
    db.drop_all()
    db.create_all()
    click.echo("Finished Creating Database")





@click.command("populate_db")
@with_appcontext
def populate_db():

    click.echo("Add Admins in Database")
    for admin in Admins:
        admin = User(name=admin[0], number=admin[1], mail=admin[2],
                    password=admin[3], adress=admin[4], Type=admin[5])
        db.session.add(admin)

    click.echo("Add Games in Database")
    for game in Games:
        game_item = Game(name=game["Name"], platform=game["platform"], condition=game["condition"],
                        exclusive=game["exclusive"], price=game["Price"], cuantity=game["cuantity"], img=game["img"])
        db.session.add(game_item)

    click.echo("Add Gifts in Database")
    for gift in Gifts:
        gift_item = Gift(name=gift["Name"], type=gift["Type"], price=gift["Price"], region=gift["Region"], img=gift["img"])
        db.session.add(gift_item)

    click.echo("Done")

    db.session.commit()

