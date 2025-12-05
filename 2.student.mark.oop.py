class Person:
    def __init__(self, _id, name, dob):
        self._id = _id
        self._name = name
        self._dob = dob

    def get_name(self):
        return self._name

    def get_id(self):
        return self._id

    def get_dob(self):
        return self._dob

    def display(self):
        print(f"ID: {self._id}, Name: {self._name}, DoB: {self._dob}")


class Student(Person):
    def __init__(self, _id, name, dob):
        super().__init__(_id, name, dob)
        self._marks = {}  

    def set_mark(self, course_id, mark):
        self._marks[course_id] = mark

    def get_mark(self, course_id):
        return self._marks.get(course_id, None)

    def display(self):
        print(f"Student: {self._id} - {self._name} ({self._dob})")

    @staticmethod
    def input_student():
        sid = input("Student ID: ")
        name = input("Student Name: ")
        dob = input("Student DoB (DD/MM/YYYY): ")
        return Student(sid, name, dob)


class Course:
    def __init__(self, _cid, _cname):
        self._cid = _cid
        self._cname = _cname

    def get_id(self):
        return self._cid

    def get_name(self):
        return self._cname

    def display(self):
        print(f"Course: {self._cid} - {self._cname}")

    @staticmethod
    def input_course():
        cid = input("Course ID: ")
        cname = input("Course Name: ")
        return Course(cid, cname)


class Mark:
    def __init__(self, student, course, score):
        self._student = student
        self._course = course
        self._score = score

    def get_student(self):
        return self._student

    def get_course(self):
        return self._course

    def get_score(self):
        return self._score

    def display(self):
        print(f"{self._student.get_name()} - {self._course.get_name()} : {self._score}")


class Mark_Management:
    def __init__(self):
        self._students = []
        self._courses = []
        self._marks = {} 


    def input_students(self):
        n = int(input("Enter number of students: "))
        for _ in range(n):
            self._students.append(Student.input_student())

    def input_courses(self):
        n = int(input("Enter number of courses: "))
        for _ in range(n):
            self._courses.append(Course.input_course())

    def select_course(self):
        if not self._courses:
            print("No courses available.")
            return None
        print("\nAvailable courses:")
        for i, c in enumerate(self._courses):
            print(f"{i+1}. {c.get_id()} - {c.get_name()}")

        idx = int(input("Select course by number: ")) - 1

        if idx < 0 or idx >= len(self._courses):
            print("Invalid selection.")
            return None

        return self._courses[idx]

    def input_marks(self, course):
        if course is None:
            print("No course selected.")
            return

        print(f"\nEntering marks for course: {course.get_name()}")

        for st in self._students:
            try:
                mark_value = float(input(f"Mark for {st.get_name()} ({st.get_id()}): "))
            except ValueError:
                print("Invalid mark! Set to 0.0")
                mark_value = 0.0

        
            m = Mark(st, course, mark_value)

      
            self._marks[(st.get_id(), course.get_id())] = m



    def list_students(self):
        print("\nSTUDENT LIST:")
        for s in self._students:
            s.display()

    def list_courses(self):
        print("\nCOURSE LIST:")
        for c in self._courses:
            c.display()

    def show_student_marks(self, course):
        if course is None:
            print("No course selected.")
            return

        print(f"\nMARKS FOR COURSE: {course.get_name()} ({course.get_id()}):")

        found = False

        for (sid, cid), mark_obj in self._marks.items():
            if cid == course.get_id():
                student = mark_obj.get_student()
                score = mark_obj.get_score()
                print(f"{student.get_name()} ({student.get_id()}): {score}")
                found = True

        if not found:
            print("No marks recorded for this course.")




def main():
    clazz = Mark_Management()

    clazz.input_students()
    clazz.input_courses()

    course = clazz.select_course()

    clazz.input_marks(course)

    clazz.list_courses()
    clazz.list_students()
    clazz.show_student_marks(course)


if __name__ == "__main__":
    main()
