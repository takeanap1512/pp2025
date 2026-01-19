import curses
import os
import zipfile
import time
from domains.models import Mark_Management
import input as ui_in
import output as ui_out


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

def list_gpa_ui(stdscr, manager):
    manager.sort_students_by_gpa()
    
    stdscr.clear()
    stdscr.addstr(0, 0, "=== STUDENT GPA RANKING ===", curses.A_BOLD)
    stdscr.addstr(1, 0, f"{'ID':<10} {'Name':<20} {'GPA':<5}")
    stdscr.addstr(2, 0, "-"*40)
    
    for i, s in enumerate(manager.get_students()):
        stdscr.addstr(i + 3, 0, f"{s.get_id():<10} {s.get_name():<20} {s.get_gpa():<5}")
        
    stdscr.addstr(len(manager.get_students()) + 5, 0, "Press any key to return.")
    stdscr.getch()

def compress_files(method_name):
    """Compresses .txt files into students.dat"""
    files_to_compress = ['students.txt', 'courses.txt', 'marks.txt']

    existing_files = [f for f in files_to_compress if os.path.exists(f)]
    
    if not existing_files:
        return 

    with zipfile.ZipFile('students.dat', 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in existing_files:
            zipf.write(file)
           
            os.remove(file)

def decompress_data():
    """Extracts students.dat if it exists"""
    if os.path.exists('students.dat'):
        with zipfile.ZipFile('students.dat', 'r') as zipf:
            zipf.extractall()
        return True
    return False

def main(stdscr):
    curses.curs_set(1)
    manager = Mark_Management()

    if decompress_data():
        ui_in.load_data(manager)
        stdscr.addstr(0, 0, "Data loaded from students.dat successfully!")
        stdscr.refresh()
        time.sleep(1)

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
            compress_options = ["Yes (Zip)", "No (Discard)"]
            sub_choice = ui_out.draw_menu(stdscr, compress_options, title="COMPRESS DATA?")
            
            if sub_choice == 1:
                compress_files("zip")
                stdscr.addstr(10, 0, "Compressed to students.dat")
                stdscr.refresh()
                time.sleep(1)
            break

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except Exception as e:
        print(f"Error: {e}")