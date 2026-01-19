import numpy as np

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