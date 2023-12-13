# university_system.py

from student import Student
from course import Course
from enrollment import Enrollment

# Create students
student1 = Student(1, "Alice", "alice@example.com")
student2 = Student(2, "Bob", "bob@example.com")

# Create courses
course1 = Course(101, "Introduction to Python")
course2 = Course(102, "Data Structures in Python")

# Create enrollments
enrollment1 = Enrollment(1001, student1, course1)
enrollment2 = Enrollment(1002, student2, course2)

# Display information
print("Enrollment Information:")
enrollment1.display_info()
print()
enrollment2.display_info()
