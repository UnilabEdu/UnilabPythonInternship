
@app.route('/step1', methods=['GET', 'POST'])
def step1():
    email = None
    first_name = None
    last_name = None

    form = registration_form()

    if form.validate_on_submit():
        session['email'] = form.email.data
        session['first_name'] = form.first_name.data
        session['last_name'] = form.last_name.data
        return redirect(url_for('step2'))

    return render_template("home.html", form=form, email=email, first_name=first_name, last_name=last_name)


@app.route('/step2', methods=['GET', 'POST'])
def step2():
    address = None
    department = None
    shift = None

    form = registration_form2()

    if form.validate_on_submit():
        session['address'] = form.address.data
        session['department'] = form.department.data
        session['shift'] = form.shift.data

        return redirect(url_for('validation'))

    return render_template("step2.html", form=form, address=address, department=department, shift=shift)


@app.route('/validation', methods=['GET', 'POST'])
def validation():
    form = final_save_to_db()

    if form.validate_on_submit():
        print(form.errors)
        new_nurse = NursesModel(session['email'], session['first_name'], session['last_name'],
                                session['address'], session['department'], session['shift'])
        db.session.add(new_nurse)
        db.session.commit()

        return redirect(url_for('step1'))

    return render_template('validation.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, port="4000")
