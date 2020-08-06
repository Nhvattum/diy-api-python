from models import app, Student
from flask import jsonify, request

@app.route('/')
def home():
    return 'This is my home.  I HAVE to defend it!'

@app.route('/nick')
def best():
    best_student = Student.query.first()
    return jsonify(student=best_student.as_dict())

@app.route('/students')
def students:
    