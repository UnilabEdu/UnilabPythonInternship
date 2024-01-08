from os import path
from flask import Blueprint, render_template, request, flash, redirect, url_for
from random import randint

from src.config import Config
from src.models import Book, Publisher, Category, Human, Author, CategoryBook, AuthorBook, PublisherBook
from src.views.library.forms import AddBookForm


TEMPLATE_FOLDER = path.join(Config.TEPMLATE_FOLDER, "library")
library_bp = Blueprint("library_bp", __name__, template_folder=TEMPLATE_FOLDER, url_prefix="/library")


@library_bp.route("/")
def library_get():
    # TODO: I should add filters
    category_ids = request.args.get("categoryIDs", None)
    author_ids = request.args.get("authorIDs", None)
    publisher_ids = request.args.get("publisherIDs", None)

    library = Book.query.filter()

    return render_template("library.html", library=library)


@library_bp.get("/library/add_book")
def add_book_get():
    form = AddBookForm()
    return render_template("add-book.html", form=form)


@library_bp.post("/library/add_book")
def add_book_post():
    form = AddBookForm()
    if form.validate_on_submit():
        title, publication_year, (author_first_name, author_last_name), category, publisher = form.title.data, form.publication_year.data ,(form.author.data.split()[0], " ".join(form.author.data.split()[1:])), form.category.data, form.publisher.data

        if not Publisher.query.filter_by(name=publisher).first():
            book_publisher = Publisher(name=publisher)
            book_publisher.create()
        else:
            book_publisher = Publisher.query.filter_by(name=publisher).first()
        if not Category.query.filter_by(name=category).first():
            book_category = Category(name=category)
            book_category.create()
        else:
            book_category = Category.query.filter_by(name=category).first()
        if not Human.query.filter_by(first_name=author_first_name, last_name=author_last_name).first():
            author_as_human = Human(first_name=author_first_name, last_name=author_last_name, birth_year=randint(1650, 2000))
            author_as_human.create()

            book_author = Author(human_id=author_as_human.id)
            book_author.create()
        else:
            author_as_human = Human.query.filter_by(first_name=author_first_name, last_name=author_last_name).first()
            book_author = Author.query.filter_by(human_id=author_as_human.id).first()


        book_to_add = Book(title=title, publication_year=publication_year)
        book_to_add.create()

        AuthorBook(book_id=book_to_add.id, author_id=book_author.id).create()
        CategoryBook(book_id=book_to_add.id, category_id=book_category.id).create()
        PublisherBook(book_id=book_to_add.id, publisher_id=book_publisher.id).create()

        flash("Book added to database successfully", "success")
        return redirect(url_for("library_bp.library_get"))
    else:
        [[flash(error, category="danger") for error in errors] for errors in form.errors.values()]
        return redirect(url_for("library_bp.add_book_get"))
