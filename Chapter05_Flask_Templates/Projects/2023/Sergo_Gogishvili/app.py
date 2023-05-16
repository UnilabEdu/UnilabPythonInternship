from flask import Flask, render_template, url_for

app=Flask(__name__)

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/about")
def about():
    names = ["fitness", "yoga", "crossfit", "pilates", "judo"]
    return render_template("about.html", list_of_names=names)



if __name__ == "__main__":
    app.run()


