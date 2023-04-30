from flask import Blueprint, render_template
from src.models.books import Book

book_blueprint = Blueprint("book", __name__, template_folder="templates")

@book_blueprint.route("/books")
def books():
    all_info  = Book.query.all()
    return render_template("books/books.html" , book_info = all_info)