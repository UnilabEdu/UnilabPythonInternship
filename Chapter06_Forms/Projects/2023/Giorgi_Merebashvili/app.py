from flask import Flask, render_template
from forms import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'DshdYAGDASNDUAY7D8DABDAGSDjhdajhd7ada'


USER_DATA = []

@app.route('/', methods=['POST', 'GET'])
def home():

    form = RegistrationForm()
    if form.validate_on_submit():
        registration_data = {
            'username': form.username.data,
            'email': form.email.data,
            'password': form.password.data
        }
        USER_DATA.append(registration_data)
    else:
        print('Not')

    return render_template('index.html', form=form)

@app.route('/admin')
def admin():

    return render_template('admin.html', users=USER_DATA)


if __name__ == '__main__':
    app.run(debug=True)