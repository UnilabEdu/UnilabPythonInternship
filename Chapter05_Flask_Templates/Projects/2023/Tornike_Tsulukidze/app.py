from flask import Flask, render_template, request


app = Flask(__name__)

bookerWinnersList = [
    {
        "year": 2022,
        "author": "Shehan Karunatilaka",
        "book": "The Seven Moons of Maali Almeida",
        "publisher": "Sort of Books"
    },
    {
        "year": 2021,
        "author": "Damon Galgue",
        "book": "The Promise",
        "publisher": "Chatto & Windus"
    },
    {
        "year": 2020,
        "author": "Douglas Stuart",
        "book": "Shuggie Bain",
        "publisher": "Picador"
    },
    {
        "year": 2019,
        "author": "Margaret Atwood",
        "book": "The Testaments",
        "publisher": "Chatto & Windus",
    },
    {
        "year": 2019,
        "author": "Bernardine Evaristo",
        "book": "Girl, Woman, Other",
        "publisher": "Hamish Hamilton"
    },
    {
        "year": 2018,
        "author": "Anna Burns",
        "book": "Milkman",
        "publisher": "Faber & Faber"
    }
]

@app.route("/")
@app.route("/home")
def main():
    return render_template("main.html", title="Home Page", bookerWinnersList=bookerWinnersList)


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)