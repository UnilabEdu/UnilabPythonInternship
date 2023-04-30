from flask import Blueprint, render_template, redirect, url_for
from app.models import Reservation
from app.book.forms import FormBook
from app import pages

book_blueprint = Blueprint('book',
                  __name__,
                  template_folder='templates/book'
                           )

thank_you_blueprint = Blueprint('thank_you',
                                __name__,
                                template_folder='templates/book'
                                )


@book_blueprint.route('/book', methods=['GET', 'POST'])
def book():

    form = FormBook()

    if form.validate_on_submit():
        name = form.name.data
        lastname = form.lastname.data
        date_from = form.date_from.data
        date_to = form.date_to.data
        select_adult = form.select_adult.data
        select_child = form.select_child.data
        reservation = Reservation(name, lastname, date_from, date_to, select_adult, select_child)
        reservation.add()

        return redirect(url_for("thank_you.thank_you"))

    return render_template('book_now.html', form=form, pages=pages)

@thank_you_blueprint.route('/thank_you')
def thank_you():
    reservations = Reservation.query.all()
    return render_template('thankyou.html', reservations=reservations)