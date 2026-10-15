
from flask import Flask, render_template, request
import sqlite3
from view_students import get_students_info

app = Flask(__name__)

def get_db():
    return sqlite3.connect("college.db")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/course")
def course():
    return render_template("course.html")

# return render_template("register.html")

@app.route("/register", methods=["POST"])
def register():
    name = request.form["name"]
    course = request.form["course"]

    con = get_db()
    con.execute(
        "INSERT INTO students (name, course) VALUES (?, ?)",
        (name, course)
    )
    con.commit()
    con.close()

    return "Student registered successfully!"


@app.route("/info")
def student_info():
    students = get_students_info()
    print(students)
    return render_template("students_info.html", students=students)
    


if __name__ == "__main__":
    app.run(debug=True)
