from flask import Flask, render_template
from resources.pages import nav_bar_pages

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', pages=nav_bar_pages)

@app.route('/add')
def add():
    return render_template('add.html', pages=nav_bar_pages)

@app.route('/items_list')
def items_list():
    return render_template('list.html', pages=nav_bar_pages)

@app.route('/update')
def update():
    return render_template('update.html', pages=nav_bar_pages)

@app.route('/delete')
def delete():
    return render_template('delete.html', pages=nav_bar_pages)

if __name__ == '__main__':
    app.run(port=7777, debug=True)
