
import sqlite3

con = sqlite3.connect("college.db")

con.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    course TEXT NOT NULL
)
""")

# Insert student details
con.execute(
    "INSERT INTO students (name, course) VALUES (?, ?)",
    ("Deepika", "B.Sc Computer Science")
)

con.commit()
con.close()

print("Student details saved successfully!")