import sqlite3

DB = None
CONN = None

def get_student_by_github(github):
    query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""
    DB.execute(query, (github,))
    row = DB.fetchone()
    return row


    ''' """\
Student: %s %s
Github account: %s"""%(row[0], row[1], row[2])
'''

def show_all_grades(first_name, last_name):
    query = """SELECT * FROM Grades
            JOIN Students ON (Grades.student_github = Students.github)
            WHERE first_name = ? AND last_name = ?"""
    DB.execute(query, (first_name, last_name))
    grades = DB.fetchall()
    list_of_grades = []
    for i in range(0, len(grades)):
        list_of_grades.append((grades[i][1], grades[i][2]))
    return list_of_grades
        # print """\
        # Project: %s     Grade: %s """ % (grades[i][1], grades[i][2])
    #return grades

def all_grades_for_project(title):
    print title
    query = """SELECT * FROM Grades
            JOIN Students ON (Grades.student_github = Students.github)
            WHERE project_title = ?"""
    DB.execute(query, (title,))
    all_grades = DB.fetchall()
    list_of_all_grades = []
    for i in range(0, len(all_grades)):
        list_of_all_grades.append((all_grades[i][3], all_grades[i][4], all_grades[i][2], all_grades[i][5]))
    return list_of_all_grades

def get_student_grade(first_name, last_name, title):
    query = """SELECT grade FROM Grades
                JOIN Students ON (Grades.student_github = Students.github) 
                WHERE first_name = ? AND last_name = ? AND project_title = ?"""
    DB.execute(query, (first_name, last_name, title))
    row = DB.fetchone()
    return """\
Student: %s %s
Project Title: %s
Grade: %s """ % (first_name, last_name, title, row[0])

def give_grade(github, title, grade):

    query = """INSERT INTO grades VALUES (?,?,?)"""

    DB.execute(query, (github, title, grade))
    CONN.commit()
    print """Sucessfully added student grade: 
    Github : %s
    Title: %s
    Grade: %s """ % (github, title, grade)



def make_new_student(first_name, last_name, github):
    query = """INSERT INTO Students VALUES (?, ?, ?)"""
    DB.execute(query, (first_name, last_name, github))
    CONN.commit()
    print "Successfully added student: %s %s" % (first_name, last_name)

def get_project_by_title(title):
    query = """SELECT title, description, max_grade FROM Projects WHERE title = ?"""
    DB.execute(query, (title,))
    row = DB.fetchone()
    print """\
Project Title: %s
Description: %s
Max Grade: %s""" % (row[0], row[1], row[2])

def add_new_project(title, description, max_grade):
    query = """INSERT INTO Projects (title, description, max_grade) VALUES (?,?,?)"""
    DB.execute(query, (title, description, max_grade))
    CONN.commit()
    print """
Successfully added project.
Title: %s
Description: %s
Max Grade %s""" % (title, description, max_grade)


def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("hackbright.db")
    DB = CONN.cursor()

def main():
    connect_to_db()
    command = None
    while command != "quit":
        input_string = raw_input("HBA Database> ")
        tokens = input_string.split()
        command = tokens[0]
        args = tokens[1:]

        if command == "student":
            get_student_by_github(*args) 
        elif command == "new_student":
            make_new_student(*args)
        elif command == "project_title":
            get_project_by_title(*args)
        elif command == "add_project":
            add_new_project(*args)
        elif command == "get_grade":
            get_student_grade(*args)
        elif command == "add_grade":
            give_grade (*args)
        elif command == "show_grades":
            show_all_grades (*args)
        elif command =="all_grades_for_project":
            all_grades_for_project(*args)

    CONN.close()

if __name__ == "__main__":
    main()
