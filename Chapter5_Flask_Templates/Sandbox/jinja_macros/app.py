from flask import Flask, render_template

serverPort = 8081

app = Flask(__name__)

nav_bar_pages_list = (
    ("home", "Home",),
    ("about", "About"),
    ("tables", "Tables")
)

table_headers = ['#', "First Name", "Last Name", "Age"]

table_rows = (
    ("0", "Temur", "Chichua", 23),
    ("1", "Giorgi", "Tskaroveli", 27),
    ("2", "Denis", "Santuryan"),
    ("3", "Ucha", "Khmaladze", 25)
)

table = {
    "headers": table_headers,
    "rows": table_rows
}


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", number=23.98, pages=nav_bar_pages_list)


@app.route('/about_us')
def about():
    return render_template("about_us.html", pages=nav_bar_pages_list)


@app.route('/tables')
def tables():
    return render_template("tables.html", pages=nav_bar_pages_list, table=table)


if __name__ == '__main__':
    app.run(port=serverPort, debug=True)
