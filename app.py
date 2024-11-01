from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory data storage for students
students = []

# Helper function to find a student by ID
def find_student(student_id):
    return next((student for student in students if student['id'] == student_id), None)

# GET /students - Retrieve a list of all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students), 200

# GET /students/{id} - Retrieve details of a student by ID
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = find_student(id)
    if student is None:
        abort(404, description="Student not found")
    return jsonify(student), 200

# POST /students - Add a new student
@app.route('/students', methods=['POST'])
def create_student():
    if not request.json or not all(k in request.json for k in ('id', 'name', 'grade', 'email')):
        abort(400, description="Invalid request data")

    new_student = {
        'id': request.json['id'],
        'name': request.json['name'],
        'grade': request.json['grade'],
        'email': request.json['email']
    }

    if find_student(new_student['id']):
        abort(400, description="Student with this ID already exists")

    students.append(new_student)
    return jsonify(new_student), 201

# PUT /students/{id} - Update an existing student by ID
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = find_student(id)
    if student is None:
        abort(404, description="Student not found")

    data = request.json
    student['name'] = data.get('name', student['name'])
    student['grade'] = data.get('grade', student['grade'])
    student['email'] = data.get('email', student['email'])

    return jsonify(student), 200

# DELETE /students/{id} - Delete a student by ID
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = find_student(id)
    if student is None:
        abort(404, description="Student not found")

    students.remove(student)
    return jsonify({'result': 'Student deleted successfully'}), 200

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': error.description}), 404

# Error handler for 400
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': error.description}), 400

if __name__ == '__main__':
    app.run(debug=True)
