from flask import Flask, render_template, url_for

app = Flask(__name__)

serverPort = 8085

pages = (
    ("home", "Home"),
    ("book", "Book now"),
    ("rooms", "Rooms"),
    ("contact", "Contact us")

)

table_headers = ["#","Room Type", "Price", "Quantity"]

table_rows = (
    (1,"Double","80$",20),
    (2,"Triple","110$",5),
    (3,"Quadruple","130$",5),
    (4,"Family","150$",4)
)

table = {
    "headers":table_headers,
    "rows":table_rows
}

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", pages=pages)

@app.route("/book")
def book():
    return render_template("book_now.html", pages=pages)

@app.route("/rooms")
def rooms():
    return render_template("room_info.html",pages=pages, table=table)

@app.route("/contact")
def contact():
    return render_template("contact_us.html", pages=pages)


if __name__=="__main__":
    app.run(port=serverPort,debug=True)