
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("college.db")

@app.route("/")
def home():
    return render_template("register.html")

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

if __name__ == "__main__":
    app.run(debug=True)