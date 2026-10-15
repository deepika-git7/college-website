
import sqlite3


def get_students_info():
    con = sqlite3.connect("college.db")
    try:
        students = con.execute("SELECT * FROM students").fetchall()
        return students
    finally:
        con.close()

