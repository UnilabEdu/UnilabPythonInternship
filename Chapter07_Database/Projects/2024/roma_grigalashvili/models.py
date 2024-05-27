from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Top_user(db.Model):
    __tablename__ = "top_user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    subject = db.Column(db.String(50), nullable=False)
