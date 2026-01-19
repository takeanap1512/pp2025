import curses
import math
import os
import pickle
import gzip
from domains.models import Student, Course 

FILE_NAME = "students.dat"

def save_data(manager):
    """Saves the manager object to a compressed binary file."""
    try:
        with gzip.open(FILE_NAME, "wb") as f:
            pickle.dump(manager, f)
    except Exception as e:

        pass

def load_data():
    """Loads the manager object from a compressed binary file."""
    if os.path.exists(FILE_NAME):
        try:
            with gzip.open(FILE_NAME, "rb") as f:
                return pickle.load(f)
        except (OSError, pickle.UnpicklingError):
            return None
    return None


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

        save_data(manager)
        
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
            
        save_data(manager)  

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
            

            save_data(manager)

            stdscr.clear()
            stdscr.addstr(0, 0, "Marks saved. Press any key.")
            stdscr.getch()
    except ValueError:
        pass