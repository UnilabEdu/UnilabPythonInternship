from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def melomane():
    print(request.endpoint)
    return render_template("Melomane.html")

@app.route("/registration")
def registration():
    print(request.endpoint)
    return render_template("registration.html")

if __name__ == "__main__":
    app.run(debug=True)

