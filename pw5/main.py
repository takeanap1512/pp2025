import curses
from domains.models import Mark_Management
import input as ui_in
import output as ui_out

def main(stdscr):
    curses.curs_set(1)
    manager = Mark_Management()

    while True:
        options = ["Input Students", "Input Courses", "Input Marks", "List Students by GPA", "Exit"]
        choice = ui_out.draw_menu(stdscr, options)
        
        if choice == 1:
            ui_in.input_student_ui(stdscr, manager)
        elif choice == 2:
            ui_in.input_course_ui(stdscr, manager)
        elif choice == 3:
            ui_in.input_marks_ui(stdscr, manager)
        elif choice == 4:
            ui_out.list_gpa_ui(stdscr, manager)
        elif choice == 5:
            break

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except Exception as e:
        print(f"Error: {e}")