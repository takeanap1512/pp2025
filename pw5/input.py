import curses
import math
import os
from domains.models import Student, Course 

def save_students_to_file(students):
    with open("students.txt", "w", encoding="utf-8") as f:
        for s in students:
            f.write(f"{s.get_id()},{s.get_name()},{s._dob}\n")

def save_courses_to_file(courses):
    with open("courses.txt", "w", encoding="utf-8") as f:
        for c in courses:
            f.write(f"{c.get_id()},{c.get_name()},{c.get_credits()}\n")

def save_marks_to_file(students):
    with open("marks.txt", "w", encoding="utf-8") as f:
        for s in students:
            marks = s.get_marks()
            for cid, mark in marks.items():
                f.write(f"{cid},{s.get_id()},{mark}\n")

def load_data(manager):
    if os.path.exists("students.txt"):
        with open("students.txt", "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) >= 3:
                    manager.add_student(Student(parts[0], parts[1], parts[2]))

    if os.path.exists("courses.txt"):
        with open("courses.txt", "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) >= 3:
                    manager.add_course(Course(parts[0], parts[1], int(parts[2])))

    if os.path.exists("marks.txt"):
        with open("marks.txt", "r", encoding="utf-8") as f:
            students = manager.get_students()
            for line in f:
                parts = line.strip().split(',')
                if len(parts) >= 3:
                    cid, sid, mark = parts[0], parts[1], float(parts[2])
                    for s in students:
                        if s.get_id() == sid:
                            s.add_mark(cid, mark)
                            break


def get_param(stdscr, prompt):
    stdscr.clear()
    stdscr.addstr(0, 0, prompt)
    curses.echo() 
    stdscr.refresh()
    input_bytes = stdscr.getstr(1, 0, 20)
    input_str = input_bytes.decode('utf-8')
    curses.noecho()
    return input_str

def input_student_ui(stdscr, manager):
    try:
        val = get_param(stdscr, "Enter number of students: ")
        if not val: return
        n = int(val)
        for i in range(n):
            sid = get_param(stdscr, f"Student {i+1} ID: ")
            name = get_param(stdscr, f"Student {i+1} Name: ")
            dob = get_param(stdscr, f"Student {i+1} DoB: ")
            manager.add_student(Student(sid, name, dob))

        save_students_to_file(manager.get_students())
        
    except ValueError:
        pass

def input_course_ui(stdscr, manager):
    try:
        val = get_param(stdscr, "Enter number of courses: ")
        if not val: return
        n = int(val)
        for i in range(n):
            cid = get_param(stdscr, f"Course {i+1} ID: ")
            name = get_param(stdscr, f"Course {i+1} Name: ")
            try:
                c_val = get_param(stdscr, f"Course {i+1} Credits: ")
                credit = int(c_val) if c_val else 0
            except ValueError:
                credit = 0
            manager.add_course(Course(cid, name, credit))
            
        save_courses_to_file(manager.get_courses())

    except ValueError:
        pass

def input_marks_ui(stdscr, manager):
    courses = manager.get_courses()
    students = manager.get_students()
    
    if not courses or not students:
        stdscr.clear()
        stdscr.addstr(0, 0, "Need students and courses first! Press any key.")
        stdscr.getch()
        return

    stdscr.clear()
    stdscr.addstr(0, 0, "Select Course to input marks for:")
    for i, c in enumerate(courses):
        stdscr.addstr(i+1, 0, str(c))
    stdscr.refresh()
    
    try:
        key = stdscr.getch()
        choice = int(chr(key)) - 1
        if 0 <= choice < len(courses):
            selected_course = courses[choice]
            for s in students:
                raw_input = get_param(stdscr, f"Mark for {s.get_name()} in {selected_course.get_name()}: ")
                try:
                    val = float(raw_input)
                    rounded_mark = math.floor(val * 10) / 10
                    s.add_mark(selected_course.get_id(), rounded_mark)
                except ValueError:
                    s.add_mark(selected_course.get_id(), 0.0)
            

            save_marks_to_file(students)

            stdscr.clear()
            stdscr.addstr(0, 0, "Marks saved. Press any key.")
            stdscr.getch()
    except ValueError:
        pass