from app import db, app, Product, User, IDCard, University, Student, Actor, Movie, MovieActor


with app.app_context():
    db.create_all()