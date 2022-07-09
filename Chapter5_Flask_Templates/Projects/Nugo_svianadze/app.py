from flask import Flask, render_template, redirect, url_for,request
from random import randint,choice

app = Flask(__name__)

nav_bar_pages = (
    ("home", "Home",),
    ('students', 'Students')
)

random_10_name = ["John", "Jane", "Mary", "Bob", "Tom", "Jack", "Jill", "Jane", "Mary", "Bob"]
random_10_age = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
random_10_subject = ["Math", "English", "Science", "History", "Art", "Music", "Computer", "Biology", "Physics", "Chemistry"]
random_10_country = ["USA", "Canada", "UK", "France", "Germany", "Italy", "Japan", "China", "Georgia", "India"]

@app.route('/')
def home():
    if request.method == "GET":
        return render_template("home.html", pages=nav_bar_pages)

@app.route('/students', methods=["GET", "POST"])
def students():
    if request.method == "POST":
        students_data = []
        student_amount = request.form["student_amount"]
        for _ in range(int(student_amount)):
            students_data.append({'name': choice(random_10_name),
                                  'age': choice(random_10_age),
                                  'subject': choice(random_10_subject),
                                  'country': choice(random_10_country),
                                  'grade': randint(5,100)})
        return render_template("students.html", students_data=students_data, pages=nav_bar_pages)
    if request.method == "GET":
        return render_template("index.html", pages=nav_bar_pages)






if __name__ == '__main__':
    app.run(debug=True)