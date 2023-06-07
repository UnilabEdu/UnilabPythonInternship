from flask import Flask, render_template, url_for
from forms import RegisterForm

app = Flask(__name__)
app.config["SECRET_KEY"]="NL"

cards = [
    {"name": "Buckwheat(100g)",
     "description": '350 k/cal'},
    {"name": "Rice(100g)",
     "description": "300 k/cal"}
]

@app.route("/",methods=["GET", "POST"])
def nutrition():
    form = RegisterForm()

    if form.validate_on_submit():

        print(form.username.data)
        print(form.goal.data)

    else:
        print(form.errors)

    return render_template("/Nutrition1010.html", form=form)


@app.route("/carbs")
def carbset():
    return render_template("/Carbset.html")


@app.route("/cards")
def macronutrients():
    return render_template("/Cards.html", card_list=cards)


if __name__ == "__main__":
    app.run()
