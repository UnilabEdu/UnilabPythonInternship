from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index(title='მთავარი'):
    return render_template('index.html', title=title)


@app.route('/archive')
def archive(title='არქივი'):
    return render_template('archive.html', title=title)


@app.route('/about')
def about(title='ჩვენს შესახებ'):
    return render_template('about.html', title=title)


if __name__ == '__main__':
    app.run(port=5050, debug=True)
