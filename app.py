

from flask import Flask, request, jsonify

app = Flask(__name__)

students = []


# GET API
@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)


# POST API
@app.route("/students", methods=["POST"])
def add_student():
    student = request.json
    students.append(student)

    return jsonify({
        "message": "Student added successfully",
        "student": student
    })


# PUT API
@app.route("/students/<int:Id>", methods=["PUT"])
def update_student(Id):

    for student in students:

        if student["Id"] == Id:

            student["Name"] = request.json["Name"]
            student["Course"] = request.json["Course"]

            return jsonify({
                "message": "Updated successfully",
                "student": student
            })

    return jsonify({
        "message": "Student not found"
    }), 404


# DELETE API
@app.route("/students/<int:Id>", methods=["DELETE"])
def delete_student(Id):

    for student in students:

        if student["Id"] == Id:

            students.remove(student)

            return jsonify({
                "message": "Deleted successfully"
            })

    return jsonify({
        "message": "Student not found"
    }), 404


if __name__ == "__main__":
    app.run(debug=True)