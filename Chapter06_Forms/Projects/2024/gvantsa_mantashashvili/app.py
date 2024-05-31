from flask import Flask, render_template
from forms import RegisterForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"

programs = [
    {"name": "პროგრამირების საფუძვლების კურსი",
     "description": "მოცემული კურსი განკუთვნილია დაწყებითი კლასების მოსწავლეებისთვის"
     },
    {"name": "Python-ის კურსი",
     "description": "კურსი მოიცავს პითონის სწავლას სკოლის მოსწავლეებისთვის."
     },
    {"name": "Html/css/js კურსი",
     "description": "კურსი განკუთვნილია ყველა დაინტერესებულისათვის 12 წლიდან."
     },
    {"name": "C++ კურსი",
     "description": "კურსი განკუთვნილია სკოლის მოსწავლეებისთვის, რომლებიც გატაცებულნი არიან რთული ამოცანების ამოხსნით"
     }
]
users = []


@app.route("/")
def home():
    return render_template("index.html", programs=programs)


@app.route("/about")
def about_page():
    return render_template("about_us.html")


@app.route("/register.html", methods=["POST", "GET"])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = {"firstname": form.firstname.data,
                    "lastname": form.lastname.data,
                    "email": form.email.data,
                    "password": form.password.data
                    }

        print(new_user)
        users.append(new_user)
    print(form.errors)
    return render_template("register.html", form=form)


@app.route("/contact.html")
def contact_page():
    return render_template("contact.html")


@app.route("/programs")
def products_page():
    return render_template("products.html", programs=programs)


@app.route("/programs/<int:id>")
def view_products_page(id):
    view_program = programs[id]
    return render_template("about_products.html", view_program=view_program)


if __name__ == "__main__":
    app.run(debug=True)
