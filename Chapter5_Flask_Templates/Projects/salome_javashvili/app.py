from flask import Flask, render_template

app = Flask(__name__)


pathogens = ['Bacteria', 'Virus', 'Fungi', 'Parasite']
pathogens_ge = ['ბაქტერია', 'ვირუსი', 'სოკო', 'პარაზიტი']

regions = ['Tbilisi', 'Kakheti', 'Inner Kartli', 'Lower Kartli', 'Mtskheta-Mtianeti', 'Imereti',
           'Samegrelo-Upper Svaneti', 'Ratcha-Lechkhumi/ Lower Svaneti', 'Samtskhe-Javakheti', 'Guria', 'Adjara']
regions_ge = ['თბილისი', 'კახეთი', 'შიდა ქართლი', 'ქვემო ქართლი', 'მცხეთა-მთიანეთი', 'იმერეთი',
           'სამეგრელო-ზემო სვანეთი', 'რაჭა-ლეჩხუმი/ ქვემო სვანეთი', 'სამცხე-ჯავახეთი', 'გურია', 'აჭარა']


@app.route('/home')
def home():
    return render_template("main.html", pathogens=pathogens, regions=regions)


@app.route('/homeGE')
def home_ge():
    return render_template("main_GE.html", pathogens=pathogens_ge, regions=regions_ge)


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/loginGE')
def login_ge():
    return render_template("login_GE.html")


@app.route('/signup')
def signup():
    return render_template("signup.html")


@app.route('/signupGE')
def signup_ge():
    return render_template("signup_GE.html")







if __name__ == "__main__":
    app.run(port=8080, debug=True)
