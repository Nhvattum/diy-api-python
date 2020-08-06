from models import app, Student
from flask import jsonify, request
from crud.post_crud import create_student

# HOME ROUTE
@app.route('/')
def home():
    return 'This is my home.  I HAVE to defend it!'

# BEST STUDENT ROUTE
@app.route('/nick')
def best():
    best_student = Student.query.first()
    return jsonify(student=best_student.as_dict())

# ALL STUDENTS ROUTE
@app.route('/students', methods=['GET', 'POST'])
def students():
    if request.method == 'GET':
        all_students = Student.query.all()
        student_list = []
        for student in all_students:
            student_list.append(student.as_dict())
        return jsonify(student_list)
    else:
        return create_student(name=request.form['name'], age=request.form['age'], location=request.form['location'], grade=request.form['grade'])


# POST ROUTE
# @app.route('/new', method='POST')
# def post():

