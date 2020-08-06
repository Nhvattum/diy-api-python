from flask import jsonify
from models import Student

def create_student(name, age, location, grade):
    new_student = Student(
        name=name, 
        age=age, 
        location=location, 
        grade=grade
    )
    db.session.add(new_student)
    db.session.commit()
    return jsonify(new_student.as_dict())