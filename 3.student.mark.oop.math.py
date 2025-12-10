import math
import numpy as np
import curses

class Person:
    def __init__(self, _id, name, dob):
        self._id = _id
        self._name = name
        self._dob = dob

    def get_name(self):
        return self._name

    def get_id(self):
        return self._id

class Student(Person):
    def __init__(self, _id, name, dob):
        super().__init__(_id, name, dob)
        self._marks = {}  
        self._gpa = 0.0

    def add_mark(self, course_id, mark):
        self._marks[course_id] = mark

    def get_marks(self):
        return self._marks
    
    def get_gpa(self):
        return self._gpa

    def set_gpa(self, gpa):
        self._gpa = gpa

    def __str__(self):
        return f"{self._name} (ID: {self._id})"

class Course:
    def __init__(self, _cid, _cname, credits):
        self._cid = _cid
        self._cname = _cname
        self._credits = credits

    def get_id(self):
        return self._cid

    def get_name(self):
        return self._cname
    
    def get_credits(self):
        return self._credits

    def __str__(self):
        return f"[{self._cid}] {self._cname} ({self._credits} credits)"

class Mark_Management:
    def __init__(self):
        self._students = []
        self._courses = []

    def add_student(self, student):
        self._students.append(student)

    def add_course(self, course):
        self._courses.append(course)

    def get_students(self):
        return self._students

    def get_courses(self):
        return self._courses

    def calculate_all_gpa(self):
        for student in self._students:
            marks_list = []
            credits_list = []
            
            student_marks = student.get_marks()
      
            for course in self._courses:
                cid = course.get_id()
                if cid in student_marks:
                    marks_list.append(student_marks[cid])
                    credits_list.append(course.get_credits())
       
            if len(marks_list) > 0:
                np_marks = np.array(marks_list)
                np_credits = np.array(credits_list)
                weighted_sum = np.sum(np_marks * np_credits)
                total_credits = np.sum(np_credits)
                if total_credits > 0:
                    gpa = weighted_sum / total_credits
                    student.set_gpa(round(gpa, 2))
                else:
                    student.set_gpa(0.0)
            else:
                student.set_gpa(0.0)

    def sort_students_by_gpa(self):
        self.calculate_all_gpa()
        self._students.sort(key=lambda x: x.get_gpa(), reverse=True)


def get_param(stdscr, prompt):
    """Helper to get string input in curses"""
    stdscr.clear()
    stdscr.addstr(0, 0, prompt)
    curses.echo() 
    stdscr.refresh()
    
    input_bytes = stdscr.getstr(1, 0, 20)
    input_str = input_bytes.decode('utf-8')
    
    curses.noecho()
    return input_str

def draw_menu(stdscr, options, title="MENU"):
    """Helper to draw a selection menu"""
    stdscr.clear()
    stdscr.addstr(0, 0, f"=== {title} ===", curses.A_BOLD)
    
    for idx, opt in enumerate(options):
        stdscr.addstr(idx + 1, 0, f"{idx + 1}. {opt}")
    
    stdscr.addstr(len(options) + 2, 0, "Select option: ")
    stdscr.refresh()
    
    key = stdscr.getch()
    return key - 48  


def input_student_ui(stdscr, manager):
    try:
        n = int(get_param(stdscr, "Enter number of students: "))
        for i in range(n):
            sid = get_param(stdscr, f"Student {i+1} ID: ")
            name = get_param(stdscr, f"Student {i+1} Name: ")
            dob = get_param(stdscr, f"Student {i+1} DoB: ")
            manager.add_student(Student(sid, name, dob))
    except ValueError:
        pass

def input_course_ui(stdscr, manager):
    try:
        n = int(get_param(stdscr, "Enter number of courses: "))
        for i in range(n):
            cid = get_param(stdscr, f"Course {i+1} ID: ")
            name = get_param(stdscr, f"Course {i+1} Name: ")
            try:
                credit = int(get_param(stdscr, f"Course {i+1} Credits: "))
            except ValueError:
                credit = 0
            manager.add_course(Course(cid, name, credit))
    except ValueError:
        pass

def input_marks_ui(stdscr, manager):
    courses = manager.get_courses()
    students = manager.get_students()
    
    if not courses or not students:
        stdscr.addstr(10, 0, "Need students and courses first! Press any key.")
        stdscr.getch()
        return

    stdscr.clear()
    stdscr.addstr(0, 0, "Select Course to input marks for:")
    for i, c in enumerate(courses):
        stdscr.addstr(i+1, 0, str(c))
    stdscr.refresh()
    
    try:
        choice = int(chr(stdscr.getch())) - 1
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
                    
            stdscr.addstr(5, 0, "Marks saved. Press any key.")
            stdscr.getch()
    except ValueError:
        pass

def list_gpa_ui(stdscr, manager):
    manager.sort_students_by_gpa()
    
    stdscr.clear()
    stdscr.addstr(0, 0, "=== STUDENT GPA RANKING ===", curses.A_BOLD)
    stdscr.addstr(1, 0, f"{'ID':<10} {'Name':<20} {'GPA':<5}")
    stdscr.addstr(2, 0, "-"*40)
    
    for i, s in enumerate(manager.get_students()):
        stdscr.addstr(i + 3, 0, f"{s.get_id():<10} {s.get_name():<20} {s.get_gpa():<5}")
        
    stdscr.addstr(i + 5, 0, "Press any key to return.")
    stdscr.getch()

def main(stdscr):
    curses.curs_set(1) 
    manager = Mark_Management()

    while True:
        options = ["Input Students", "Input Courses", "Input Marks", "List Students by GPA", "Exit"]
        choice = draw_menu(stdscr, options)
        
        if choice == 1:
            input_student_ui(stdscr, manager)
        elif choice == 2:
            input_course_ui(stdscr, manager)
        elif choice == 3:
            input_marks_ui(stdscr, manager)
        elif choice == 4:
            list_gpa_ui(stdscr, manager)
        elif choice == 5:
            break

if __name__ == "__main__":
    curses.wrapper(main)