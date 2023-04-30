from flask import render_template, Blueprint

homepage = Blueprint('homepage',
                     __name__,
                     template_folder='templates/homepage')


@homepage.route('/', methods=['GET'])
def representation():
    return render_template("represent.html")
