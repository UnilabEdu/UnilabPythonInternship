from flask import Flask, render_template, request, flash
from models import Faculty, app

#ვებ გვერდის ჩატვირთვა და ბაზის ყველა მონაცემის ჩვენება 
@app.route('/')
def index():
    return render_template("index.html")
    

@app.route('/registrate')
def registrate():
    return render_template("registrate.html")

@app.route('/allactive')
def allstudent():

    students = Faculty.query.order_by(Faculty.id).all()
       
    return render_template("allactive.html", students = students)

if __name__ == '__main__':
    app.run(debug=True)