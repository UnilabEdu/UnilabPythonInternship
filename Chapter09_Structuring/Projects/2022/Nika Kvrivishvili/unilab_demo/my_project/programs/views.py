from flask import Blueprint, render_template, redirect, url_for
from my_project.programs.forms import ProgramForm
from my_project.programs.models import Program

program_blueprint = Blueprint('programs',
                              __name__,
                              template_folder='templates/programs')


@program_blueprint.route('/admin', methods=['GET', 'POST'])
def admin():
    form = ProgramForm()

    if form.validate_on_submit():
        program = form.program.data

        add_program = Program(program)
        add_program.add()

        form.program.data = ''

        redirect(url_for('programs.admin'))

    return render_template('admin.html', form=form)
