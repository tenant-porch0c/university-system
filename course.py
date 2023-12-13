# course.py

class Course:
    def __init__(self, course_id, title):
        self.course_id = course_id
        self.title = title

    def display_info(self):
        print(f"Course ID: {self.course_id}")
        print(f"Title: {self.title}")
