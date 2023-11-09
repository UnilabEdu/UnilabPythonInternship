from flask import Flask, render_template, request

app = Flask(__name__)

SPORTS = [
    'Basketball', 'Football', 'Volleyball'
]

REGISTRANTS = [{}]

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        sport = request.form.get('sport')

        REGISTRANTS[0]['name'] = name
        REGISTRANTS[0]['sport'] = sport

    return render_template('index.html', sports=SPORTS)


@app.route('/registrants')
def registrants():

    return render_template('registrants.html', registrants=REGISTRANTS)


if __name__ == '__main__':
    app.run(debug=True)