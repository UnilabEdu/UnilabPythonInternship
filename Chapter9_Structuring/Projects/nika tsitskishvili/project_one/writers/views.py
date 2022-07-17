from project_one.writers.models import Writer
from flask import render_template, Blueprint
from project_one.writers.forms import FilterTable
writers_blueprint = Blueprint('writers', __name__, static_folder='static', template_folder='templates')

@writers_blueprint.route("/create", methods=["GET","POST"])
def create():
    myform = FilterTable()
    if myform.validate_on_submit() and myform.submit.data:
        name = myform.name.data
        Writer.create(name=name)
    else:
        pass
    return render_template("create.html", myform=myform)


@writers_blueprint.route("/read", methods=["GET","POST"])
def read():
    myform = FilterTable()
    data, author = None, None
    name = myform.name.data
    if myform.validate_on_submit() and myform.submit.data:
        data = Writer.read(name=name)
    else:
        pass
    return render_template("read.html", data=data, myform=myform)


@writers_blueprint.route("/update", methods=["GET","POST"])
def update():
    myform= FilterTable()
    if myform.validate_on_submit() and myform.submit.data:
        name = myform.name.data
        new_name = myform.new_name.data
        Writer.update(name=name, new_name=new_name)
    else:
        pass
    return render_template("update.html", myform=myform)



@writers_blueprint.route("/delete", methods=["GET","POST"])
def delete():
    myform = FilterTable()
    if myform.validate_on_submit() and myform.submit.data:
        name = myform.name.data
        Writer.delete(name)
    return render_template("delete.html", myform=myform)
