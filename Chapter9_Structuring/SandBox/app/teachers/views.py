from flask import Blueprint

teachers_blueprint = Blueprint('teachers',
                               __name__,
                               template_folder='templates/teachers'
                               )

