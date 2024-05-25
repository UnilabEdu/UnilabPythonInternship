from app import app, db, products

with app.app_context():
    db.create_all()