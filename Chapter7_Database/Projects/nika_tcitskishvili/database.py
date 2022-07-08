from app import db, app
from model import SubjectModel, TeacherModel, StudentModel
from data import teacher_data, student_data, subject_data

def create_database():
    for i in teacher_data:
        teacher = TeacherModel(first_name=i["first_name"], last_name=i["last_name"], subject_id=i["subject_id"])
        db.session.add(teacher)
        db.session.flush()
    for i in student_data:
        student = StudentModel(first_name=i["first_name"], last_name=i["last_name"], subject_id=i["subject_id"])
        db.session.add(student)
        db.session.flush()
    for i in subject_data:
        for j in student_data:
            if j["subject_id"] == i["id"]:
                i["students"].append(j["first_name"]+" "+j["last_name"]+",")
        i["students"] = ' '.join(i["students"])
        for k in teacher_data:
            if k["subject_id"] == i["id"]:
                i["teacher"].append(k["first_name"]+" "+k["last_name"])
        i["teacher"] = ' '.join(i["teacher"])
        subject = SubjectModel(id=i["id"], title=i["title"], students=i["students"], teacher=i["teacher"])
        db.session.add(subject)
        db.session.commit()



