from flask import Flask, render_template, request, flash
from .forms import RegistrtionForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissecret'  # თუ დაგჭირდებათ და რამეში გამოგადეგაბთ აქ არის <3 

#ვებ გვერდის ჩატვირთვა და ბაზის ყველა მონაცემის ჩვენება 
@app.route('/')
def index():
    return render_template("index.html")
    

@app.route('/registrate')
def registrate():
    return render_template("registrate.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrtionForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)