def input_number_of_students():
    return int(input("Enter number of students: "))

def input_student_information():
    student_id = input("Student ID: ")
    student_name = input("Student Name: ")
    student_dob = input("Student DoB (DD/MM/YYYY): ")
    return {"id": student_id, "name": student_name, "dob": student_dob}

def input_number_of_courses():
    return int(input("Enter number of courses: "))

def input_course_information():
    course_id = input("Course ID: ")
    course_name = input("Course Name: ")
    return {"id": course_id, "name": course_name}

def select_course(courses):
    print("Available courses:")
    for i, c in enumerate(courses):
        print(f"{i+1}. {c['id']} - {c['name']}")
    idx = int(input("Select course by number: ")) - 1
    return courses[idx]
def input_marks_for_course(students):
    marks = {}
    print("Enter marks for each student:")
    for st in students:
        mark = float(input(f"Mark for {st['name']} ({st['id']}): "))
        marks[st['id']] = mark
        return marks

def list_courses(courses):
    print("\nCOURSE LIST:")
    for c in courses:
        print(f"{c['id']} - {c['name']}")


def list_students(students):
    print("\nSTUDENT LIST:")
    for s in students:
        print(f"{s['id']} - {s['name']} - {s['dob']}")


def show_student_marks(course, marks, students):
    print(f"\nMARKS FOR COURSE: {course['name']} ({course['id']})")
    for st in students:
        sid = st['id']
        if sid in marks:
            print(f"{st['name']} ({sid}): {marks[sid]}")
        else:
            print(f"{st['name']} ({sid}): No mark recorded")

def main():
    students = []
    courses = []
    course_marks = {} 

    n_students = input_number_of_students()
    for _ in range(n_students):
        students.append(input_student_information())

    n_courses = input_number_of_courses()
    for _ in range(n_courses):
        courses.append(input_course_information())

    selected_course = select_course(courses)
    marks = input_marks_for_course(students)
    course_marks[selected_course['id']] = marks


    list_courses(courses)
    list_students(students)
    show_student_marks(selected_course, marks, students)

if __name__ == "__main__":
    main()