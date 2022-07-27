from models import Register
from flask import render_template, Blueprint
from forms import RegisterTable
reg_blueprint = Blueprint('register', __name__, static_folder='static', template_folder='templates')


@reg_blueprint.route("/register", methods=["GET","POST"])
def create():
    regform = RegisterTable()
    if regform.validate_on_submit() and regform.submit.data:
        name = regform.name.data
        email = regform.email.data
        password = regform.password.data
        confirm_password = regform.confirm_password.data
        if password == confirm_password:
            Register.create(name=name, email=email, password=password)
    else:
        pass
    return render_template("create.html", regform=regform)