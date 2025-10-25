# 🎓 Advanced Student Management System in Python
This project is an upgraded Object-Oriented Programming (OOP) example that demonstrates how to manage students in a school using Python.
It includes advanced Python features such as @property, @classmethod, @staticmethod, and a custom @logdecorator for automatic logging.

## 🚀 Features
- Add, remove, and search for students
- Update grades safely with validation
- Calculate average grades
- Automatically log function calls and results to log.txt
- Create students using a factory method (from_string)
- Validate data using static methods (is_valid_age, is_valid_grade)


# 🧠 Concepts Covered
- Encapsulation using private attributes (_name, _age, _grade)
- @property → for controlled attribute access
- @classmethod → to create objects from formatted strings
- @staticmethod → for validation methods
- Decorators → for logging function calls
- File handling → to record actions in a log file

## Example
```python
from main import Student, School
# Create students
s1 = Student("John", 22, 20)
s2 = Student("Zahra", 28, 19)
s3 = Student.from_string("Fati-23-18")

# Update student info
s1.grade = 19
s1.age = 23

# Create school and add students
school = School("Winter School")
school.add_student(s1)
school.add_student(s2)
school.add_student(s3)

# Show students and calculate average grade
school.show_students()
print("Average Grade:", school.average_grade())
```
# 🧾 Log File Example (log.txt)
```text
name of the function --> from_string
2025-10-25 09:55:24.560545
result: Fati | Age: 23 | Grade: 18
args: (<class '__main__.Student'>, 'Fati-23-18')
kwargs: {}
--------------------------------------------------
name of the function --> add_student
2025-10-25 09:55:24.563334
result: None
args: (<__main__.School object at 0x000001D5FFBEF280>, <__main__.Student object at 0x000001D5FFBEF0D0>)
kwargs: {}
--------------------------------------------------
name of the function --> average_grade
2025-10-25 09:55:24.569102
result: 19.00
args: (<__main__.School object at 0x000001D5FFBEF280>,)
kwargs: {}
--------------------------------------------------
```
# 🔮 Future Improvements
- Implement a command-line or GUI interface
- Add more detailed validation and exception handling

#  👩‍💻 Author
Zahra Betvan
Learning Python step by step with a focus on OOP and clean, maintainable code.