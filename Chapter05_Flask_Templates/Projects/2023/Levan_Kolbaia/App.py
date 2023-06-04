from flask import Flask, render_template, url_for

app = Flask(__name__)

cards = [
    {"name": "Buckwheat(100g)",
     "description": '350 k/cal'},
    {"name": "Rice(100g)",
     "description": "300 k/cal"}
]

@app.route("/")
def nutrition():
    return render_template("/Nutrition1010.html")


@app.route("/carbs")
def carbset():
    return render_template("/Carbset.html")


@app.route("/cards")
def macronutrients():
    return render_template("/Cards.html", card_list=cards)


if __name__ == "__main__":
    app.run()
