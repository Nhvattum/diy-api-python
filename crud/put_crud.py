from flask import jsonify
from models import Student

def update_student(name, age, location, grade):
  student = Student.query.get(id)
  if student:
    student.name = name or student.name
    student.age = age or student.age
    student.location = location or student.location
    student.grade = grade or student.grade
    db.session.commit()
    return jsonify(student.as_dict())
  else:
    raise Exception('No User at id {}'.format(id))