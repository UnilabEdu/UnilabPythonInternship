from flask import Flask, render_template, redirect, url_for, flash
from forms import RegisterForm, LoginForm, AddBookForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET"

NAVBAR_ITEMS = [
    {"endpoint": "main", "title": "Home"},
    {"endpoint": "register_get", "title": "Register"},
    {"endpoint": "login", "title": "Login"},
    {"endpoint": "library_get", "title": "Library"}
]

LIBRARY = [
    {"title": "A Clockwork Orange", "author": "Anthony Burges"},
    {"title": "Crime and Punishment", "author": "Fyodor Dostoevsky"},
    {"title": "1984", "author": "George Orwell"},
    {"title": "Ishmael", "author": "Daniel Quinn"},
    {"title": "The Red and the BLack", "author": "Sthendal"}
]


@app.context_processor
def inject_navbar_items():
    return dict(navbar_items=NAVBAR_ITEMS)


@app.route("/")
@app.route("/home")
def main():
    return render_template("main.html", title="Home Page")


@app.get("/register")
def register_get():
    form = RegisterForm()
    return render_template("register.html", form=form)


@app.post("/register")
def register_post():
    form = RegisterForm()
    if form.validate_on_submit():
        flash("Your account registered successfully", "success")
        return redirect(url_for("login"))
    else:
        [[flash(error, category="danger") for error in errors] for errors in form.errors.values()]
        return redirect(url_for("register_get", form=form))


@app.route("/login")
def login():
    return render_template("login.html")


@app.get("/library")
def library_get():
    return render_template("library.html", library=LIBRARY)


@app.get("/library/add_book")
def add_book_get():
    form = AddBookForm()
    return render_template("add-book.html", form=form)


@app.post("/library/add_book")
def add_book_post():
    form = AddBookForm()
    if form.validate_on_submit():
        LIBRARY.append({"title": form.title.data, "author": form.author.data})
        flash("Book added successfully", "success")
        return redirect(url_for("library_get"))
    else:
        [[flash(error, category="danger") for error in errors] for errors in form.errors.values()]
        return redirect(url_for("add_book_get"))



if __name__ == "__main__":
    app.run(debug=True)
