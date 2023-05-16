import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(basedir, "app.db"))

app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey"
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)


class Book(db.Model):
    title = db.Column(db.String(100), unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        return f"<Title: {self.title}>"


@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        book = Book(title=request.form.get("title"))
        db.session.add(book)
        db.session.commit()
    books = Book.query.all()
    return render_template("home.html", books=books)


@app.route("/update", methods=["POST"])
def update():
    newtitle = request.form.get("newtitle")
    oldtitle = request.form.get("oldtitle")
    book = Book.query.filter_by(title=oldtitle).first()
    book.title = newtitle
    db.session.commit()
    return redirect("/")


@app.route("/delete", methods=["POST"])
def delete():
    title = request.form.get("title")
    book = Book.query.filter_by(title=title).first()
    db.session.delete(book)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
