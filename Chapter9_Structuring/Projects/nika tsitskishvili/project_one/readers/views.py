from project_one.readers.models import Reader
from flask import render_template, Blueprint
from project_one.readers.forms import FilterTable
readers_blueprint = Blueprint('readers', __name__, static_folder='static', template_folder='templates')

@readers_blueprint.route("/create", methods=["GET","POST"])
def create():
    myform = FilterTable()
    if myform.validate_on_submit() and myform.submit.data:
        name = myform.name.data
        Reader.create(name=name)
    else:
        pass
    return render_template("create.html", myform=myform)


@readers_blueprint.route("/read", methods=["GET","POST"])
def read():
    myform = FilterTable()
    data, author = None, None
    name = myform.name.data
    if myform.validate_on_submit() and myform.submit.data:
        data = Reader.read(name=name)
    else:
        pass
    return render_template("read.html", data=data, myform=myform)


@readers_blueprint.route("/update", methods=["GET","POST"])
def update():
    myform= FilterTable()
    if myform.validate_on_submit() and myform.submit.data:
        name = myform.name.data
        new_name = myform.new_name.data
        Reader.update(name=name, new_name=new_name)
    else:
        pass
    return render_template("update.html", myform=myform)



@readers_blueprint.route("/delete", methods=["GET","POST"])
def delete():
    myform = FilterTable()
    if myform.validate_on_submit() and myform.submit.data:
        name = myform.name.data
        Reader.delete(name)
    return render_template("delete.html", myform=myform)

