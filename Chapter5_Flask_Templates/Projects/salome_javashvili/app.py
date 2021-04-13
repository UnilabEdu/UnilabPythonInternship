from flask import Flask, render_template
import data
from functions import create_dicts
app = Flask(__name__)


menu_data = create_dicts(data.select_menu_keys, data.select_menu_values)
print(menu_data)
menu_data_ge = create_dicts(data.select_menu_keys, data.select_menu_values_ge)

form_data = create_dicts(data.input_form_keys, data.input_form_values)
print(form_data)
form_data_ge = create_dicts(data.input_form_keys, data.input_form_values_ge)

@app.route('/home')
def home():
    return render_template("main.html", pathogens=data.pathogens, menu_data=menu_data, form_data=form_data)


@app.route('/home_ge')
def home_ge():
    return render_template("main_GE.html", pathogens=data.pathogens_ge, menu_data=menu_data_ge, form_data=form_data_ge)

@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/login_ge')
def login_ge():
    return render_template("login_GE.html")


@app.route('/signup')
def signup():
    return render_template("signup.html")


@app.route('/signup_ge')
def signup_ge():
    return render_template("signup_GE.html")


if __name__ == "__main__":
    app.run(port=8080, debug=True)
