import curses

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