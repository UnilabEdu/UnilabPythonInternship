from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)



user_list = {
    'otojojishvili@gmail.com' : "12345678",
    'giorgigiorgashvili@gmail.com' : "giogio",
    'bekabeka@gmail.com' : "bequsha123"
}


@app.route("/home")
def home():
    return render_template("first.html")

@app.route('/',methods = ['POST','GET'])
def index():
    if request.method == "POST":
        mail = request.form['mail']
        password = request.form['password']
        if mail in user_list and password == user_list[mail]:
            return redirect(url_for('home'))
    return render_template('sign.html', user_list = user_list)



@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)