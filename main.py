from student import Student
from  school import School


# Create students
s1 = Student("John", 22, 20)
s2 = Student("Zahra", 28, 19)
s3 = Student.new_stu("Fati-23-18")

# Update student info safely with transactions
with s1 as student:
    student.set_grade(19)
    student.age = 23

# Create school and manage students
school = School("Winter School")
school.add_student(s1)
school.add_student(s2)
school.add_student(s3)

# Remove a student safely
try:
    school.remove_student(s2)
except Exception as e:
    print("Error:", e)

# Show students and calculate average grade
school.show_students()
print("Average Grade:", school.average_grade())

# Show transaction history
school.show_history()
