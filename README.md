# 🎓 Advanced Student Management System in Python
This project is an advanced student management system demonstrating Object-Oriented Programming (OOP) concepts in Python.
It includes error handling, transaction management with rollback, and automatic logging.

## 🚀 Features
- Add, remove, and search for students
- Safely update grades and age with validation
- Manage student updates using context managers (with)
- Rollback changes automatically if an error occurs
- Calculate average grades
- Automatically log all operations and exceptions in log.txt using @logdecorator
- Create students using a factory method (from_string)



# 🧠 Concepts Covered
- Encapsulation using private attributes (_name, _age, _grade)
- @property → for controlled attribute access
- @classmethod → to create objects from formatted strings
- Decorators → Automatic logging of function calls and exceptions
- Context Managers (with) → Transaction management with rollback on error
- File handling → to record actions in a log file



## 📂 Project Structure
school_project/
│
├─ student.py       → Student class with context manager and transaction handling
├─ school.py        → School class with student management
├─ main.py          → Program execution and examples
├─ log.txt          → Log file
└─ README.md        → Project description

## Example
```python
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

```
# 🧾 Log File Example (log.txt)
```text

time--->2025-10-27 13:32:11.712798
owner--->John
function name--->set_grade
Status--->SUCCESS
grade--->19
----------------------------------------------------------------------------------------------------
time--->2025-10-27 13:32:11.714401
owner--->Winter School
function name--->add_student
Status--->SUCCESS
grade--->None
----------------------------------------------------------------------------------------------------
time--->2025-10-27 13:32:11.715838
owner--->Winter School
function name--->add_student
Status--->SUCCESS
grade--->None
----------------------------------------------------------------------------------------------------
time--->2025-10-27 13:32:11.717836
owner--->Winter School
function name--->add_student
Status--->SUCCESS
grade--->None
----------------------------------------------------------------------------------------------------
time--->2025-10-27 13:32:11.719778
owner--->Winter School
function name--->remove_student
Status--->SUCCESS
grade--->None
----------------------------------------------------------------------------------------------------
```
# 🔮 Future Improvements
- Implement a command-line or GUI interface
- Add more detailed validation and exception handling
- storage data in JSON file 

#  👩‍💻 Author
Zahra Betvan
Learning Python step by step with a focus on OOP and clean, maintainable code.