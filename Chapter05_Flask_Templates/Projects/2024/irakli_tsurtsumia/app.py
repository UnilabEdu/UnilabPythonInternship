from flask import Flask, render_template

app = Flask(__name__)

data = [
    {"name": "Lizzard", "sale": False, "price": 100, "img": "/static/MainBefore.jpg", "id": 1},
    {"name": "Gizzard", "sale": True, "price": 200, "img": "/static/MainBefore.jpg", "id": 2},
    {"name": "Wizzard", "sale": False, "price": 300, "img": "/static/MainBefore.jpg", "id": 3},
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/products')
def products():
    return render_template('products.html', products_list=data)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/product/<int:id>')
def product(id):
    return render_template("product.html", product=data[id])


if __name__ == "__main__":
    app.run(debug=True)

# დავალება
# Chapter05-ის პროექტების ფოლდერში დაამატეთ თქვენი ფოლდერი.
#
# pip-ის საშუალებით დააყენეთ Flask ბიბლიოთეკა, შემდეგ კი თქვენს ფოლდერში შექმენით app.py ფაილი, სადაც გამართავდ თქვენს სერვერს.
# მიაბით თქვენს ფლასკის აპლიკაციას წინა დავალებაზე შექმნილი HTML ფაილები (თუ გსურთ, შეგიძლიათ ახალი შექმნათ). სერვერზე უნდა გქონდეთ მინიმუმ 3 გვერდი.
#
# შექმენით base.html ფაილი სადაც გაიტანთ თქვენი საიდის მთავარ "ჩარჩოს" (ანუ html, head, body და ა.შ), ხოლო განმეორებადი ელემენტები როგორიცაა
# navbar-ი შეგიძლიათ ასევე ცალკე ფაილად გაიტანოთ და include-ის საშალებით შემოიტანოთ თქვენს base შაბლონში
#
# მინიმუმ 1 HTML გვერდს მაინც ინფორმაცია უნდა გადაეცემოდეს ბექზე შექმნილი ცვლადისგან, და Jinja-ს საშუალებით გამოდიოდეს გვერდზე.
