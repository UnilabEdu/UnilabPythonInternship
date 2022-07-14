from flask import Flask, render_template, redirect, url_for
from resources.pages import nav_bar_pages
from forms import AddForm, DeleteForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'my_secret_key'

@app.route('/')
def home():
    return render_template('home.html', pages=nav_bar_pages)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        age = form.age.data
        email = form.email.data
        return redirect(url_for('items_list'))

    return render_template('add.html', pages=nav_bar_pages, form=form)

@app.route('/items_list', methods=['GET', 'POST'])
def items_list():
    return render_template('list.html', pages=nav_bar_pages)

@app.route('/update', methods=['GET', 'POST'])
def update():
    form = AddForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        age = form.age.data
        email = form.email.data
        return redirect(url_for('items_list'))

    return render_template('update.html', pages=nav_bar_pages, form=form)

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    form = DeleteForm()
    if form.validate_on_submit():
        id = form.id.data
        return redirect(url_for('items_list'))

    return render_template('delete.html', pages=nav_bar_pages, form=form)

if __name__ == '__main__':
    app.run(port=7777, debug=True)
