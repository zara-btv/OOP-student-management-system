
from school_models.School import School
from school_models.Student import Student
from school_models.Student import Student
from school_models.School import School

# Create students
s1 = Student("John", 22, 20)
s2 = Student("Zahra", 28, 19)
s3 = Student.new_stu("Mary-20-10")

# Update student safely with rollback support
with s1 as student:
    student.grade = 19
    student.age = 23

# Manage school
school = School("Winter School")
school.add_student(s1)
school.add_student(s2)
school.add_student(s3)

# Remove safely
try:
    school.remove_student(s2)
except Exception as e:
    print("Error:", e)

# Show all students
school.show_participates()

# Calculate average grade
print("Average Grade:", school.average_grade())