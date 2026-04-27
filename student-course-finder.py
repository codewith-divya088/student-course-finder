import sqlite3

# connect to database
conn = sqlite3.connect("college.db")
cursor = conn.cursor()

# create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    course_id INTEGER
)
""")

conn.commit()

# menu
while True:
    print("\n1. Add Course")
    print("2. Add Student")
    print("3. Show Students with Courses")
    print("4. Search Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        course = input("Enter course name: ")
        cursor.execute("INSERT INTO courses (name) VALUES (?)", (course,))
        conn.commit()
        print("Course added")

    elif choice == "2":
        name = input("Enter student name: ")
        course_id = int(input("Enter course id: "))
        cursor.execute("INSERT INTO students (name, course_id) VALUES (?, ?)", (name, course_id))
        conn.commit()
        print("Student added")

    elif choice == "3":
        cursor.execute("""
        SELECT students.name, courses.name
        FROM students
        JOIN courses ON students.course_id = courses.id
        """)
        rows = cursor.fetchall()

        print("\nStudents and Courses:")
        if rows:
            for row in rows:
                print(row)
        else:
            print("No data found")

    elif choice == "4":
        name = input("Enter name to search: ")
        cursor.execute("""
        SELECT students.name, courses.name
        FROM students
        JOIN courses ON students.course_id = courses.id
        WHERE students.name LIKE ?
        """, ('%' + name + '%',))

        rows = cursor.fetchall()

        print("\nSearch Results:")
        if rows:
            for row in rows:
                print(row)
        else:
            print("No matching student found")

    elif choice == "5":
        break

    else:
        print("Invalid choice")

# close connection
conn.close()
