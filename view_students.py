
import sqlite3

con = sqlite3.connect("college.db")

students = con.execute("SELECT * FROM students")

for student in students:
    print(student)

con.close()