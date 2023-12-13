# enrollment.py

from student import Student
from course import Course

class Enrollment:
    def __init__(self, enrollment_id, student, course):
        self.enrollment_id = enrollment_id
        self.student = student
        self.course = course

    def display_info(self):
        print(f"Enrollment ID: {self.enrollment_id}")
        self.student.display_info()
        self.course.display_info()
