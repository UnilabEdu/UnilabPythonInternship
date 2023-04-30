from flask import Blueprint, render_template
from src.models.school import Teacher, Student

teachers_blueprint = Blueprint("teacher", __name__, template_folder="templates")

@teachers_blueprint.route("/teachers")
def teachers():
    teacher = Teacher.query.get(1)

    # მოდელში გაწერილ db.relationship-ით შეგვიძლია მივწვდეთ ყველა იმ სტუდენტს, სადაც teacher_id ემთხვევა teacher.id-ს
    print(teacher.students)

    students = Student.query.all()
    # ხოლო backref-ში გაწერილი ატრიბუტით, შეგვიძლია პირიქითაც წამოვიღოთ, ანუ student-დან წამოვიღოთ შესაბამისი teacher
    print(students[0].teacher)

    # ამ ატრიბუტებზე წვდომა Jinja-შიც გაქვთ, იხილეთ HTML ფაილი
    return render_template("teachers/teacher.html", teacher=teacher, students=students)