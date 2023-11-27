from flask import render_template

from models import app, db,  Registrant
from forms import RegistrationForm

with app.app_context():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def index():
    form = RegistrationForm()
    if  form.validate_on_submit():
        registrant = Registrant(
            name=form.name.data, age=form.age.data, sport=form.sport.data
        )
        db.session.add(registrant)
        db.session.commit()

    return render_template('index.html', form=form)

@app.route('/registrants')
def registrants():
    _registrants = Registrant.query.all()

    return render_template('registrants.html', registrants=_registrants)


if __name__ == '__main__':
    app.run(debug=True)