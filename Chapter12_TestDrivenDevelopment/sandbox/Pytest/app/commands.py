import click
from flask.cli import with_appcontext
from app.ext import db
from app.models.user import User
from app.models.movie import Movie


def init_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

    dummy_user = User("user", "testmail@mail.com", "password123")
    dummy_user.create(commit=True)


def populate_movies():

    movies = [
        {
            "name": "Thor: Love and Thunder",
            "genre": "Action",
            "rating": 6.8,
            "picture": "thor.jpg"
        },
        {
            "name": "Paws of Fury",
            "genre": "Comedy",
            "rating": 5.6,
            "picture": "pawsoffury.jpg"
        },
        {
            "name": "The Adam Project",
            "genre": "Adventure",
            "rating": 7.4,
            "picture": "adamproject.jpg"
        },
        {
            "name": "In Search of Tomorrow",
            "genre": "Sci-Fi",
            "rating": 9.8,
            "picture": "searchoftomorrow.jpg"
        },
        {
            "name": "Texas Chainsaw Massacre",
            "genre": "Horror",
            "rating": 8.1,
            "picture": "texaschainsawmassacre.jpg"
        },
        {
            "name": "Death on The Nile",
            "genre": "Mystery",
            "rating": 6.6,
            "picture": "deathonthenile.jpg"
        },
    ]

    for movie in movies:
        dummy_movie = Movie(movie['name'], movie['genre'], movie['rating'], movie['picture'])
        dummy_movie.create(commit=True)


@click.command('init_db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo("Created database")


@click.command('populate_movies')
@with_appcontext
def populate_movies_command():
    populate_movies()
    click.echo("Populated database with movies")


