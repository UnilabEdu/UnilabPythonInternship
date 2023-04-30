from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from forms import UserForm


app = Flask(__name__)
app.secret_key = 'mysecretkey'
WTF_CSRF_ENABLED = False
WTF_CSRF_SECRET_KEY = 'a random string'

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        form = UserForm(request.form)
        data = {'username': form.username.data,
                'email': form.email.data,
                'first_name': form.first_name.data,
                'last_name': form.last_name.data,
                'course': form.course.data,
                'university': form.university.data}
        file = form.file.data
        print(file)
        if file:
            file.save(f'{data["username"]}.png')

        return render_template('users.html', data=data)
    form = UserForm()
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)