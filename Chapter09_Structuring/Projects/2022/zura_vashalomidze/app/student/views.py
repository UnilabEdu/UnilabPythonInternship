from flask import url_for, render_template, redirect, Blueprint
from app.models import Student
from app.student.forms import LoginForm, DelForm, UpdatelForm

students_blueprint = Blueprint("student", __name__, template_folder='templates/students')

@students_blueprint.route("/")
def home():
    return render_template("home.html")


@students_blueprint.route("/add", methods=["GET", "POST"])
def add():
    myform = LoginForm()
    if myform.validate_on_submit():
        name = myform.login.data
        email = myform.email.data
        password = myform.password.data
        new_stu = Student(name, email, password)
        new_stu.save_to_db()
        return redirect(url_for("student.stu_list"))
    return render_template("add_form.html", form=myform)


@students_blueprint.route("/stu")
def stu_list():
    students = Student.query.all()
    return render_template("stu_list.html", students=students)


@students_blueprint.route("/delete", methods=['GET', 'POST'])
def delete():
    delform = DelForm()
    if delform.validate_on_submit():
        # name = myform.name.data
        name = delform.name.data
        del_stu = Student.query.filter_by(name=name).first()
        print(del_stu)
        # del_stu = Student.query.filter_by(name=name)
        del_stu.delete_from_db()
        return redirect(url_for("student.stu_list"))

    return render_template("delete.html", form=delform)


@students_blueprint.route('/update', methods=['GET', 'POST'])
def update():
    update_form = UpdatelForm()
    if update_form.validate_on_submit():
        name = update_form.name.data
        stu_id = update_form.id.data
        stu_email = update_form.email.data
        stu_update = Student.query.filter_by(id=stu_id).first()
        print(type(stu_email), f'email is {stu_email}')
        if name is not '':
            stu_update.name = name
        if stu_id is not '':
            stu_update.id = stu_id
        if stu_email is not '':
            stu_update.email = stu_email

        stu_update.save_to_db()
        return redirect(url_for("student.stu_list"))
    return render_template('update.html', form=update_form)



