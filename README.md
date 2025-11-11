# 🎓 Advanced Student Management System in Python
This project is an advanced, modular student management system built with Python OOP principles.
It includes context-managed transactions, automatic logging, JSON & CSV serialization, and custom error handling — all organized in a clean, extensible architecture.

## 🚀 Features
🧍‍♀️ Manage Students (Add / Remove / Update / Grade Tracking)
🔁 Safe operations with automatic rollback using with statement
🧾 Save and load full school state using Pickle (student_info.pickle) and CSV (grades.csv)
🪵 Automatic operation logging in log.json via a custom @logdecorator
🏫 School class for handling multiple students and calculating averages
🧱 Modular architecture (school_core, school_models, school_data)
⚙️ Strong validation and exception handling using custom error classes



# 🧠 Concepts Covered
- Encapsulation → private attributes (_name, _age, _grade)
- @property / @setter → safe attribute management
- @classmethod → class factory for creating new students
- @staticmethod / Decorators → automatic logging of actions
- Context Managers → rollback on error (__enter__ / __exit__)
- Serialization → save/load data via JSON
- CSV Handling → track grade changes over time
- Custom Exceptions → NegativeValueError, AmountValueError, ValueTypeError



## 📂 Project Structure
Student_Management_System/
│
├── main.py                         # Program entry point
│
├── school_models/
│   ├── Student.py                   # Student class with context manager & CSV logging
│   └── School.py                    # School class with JSON persistence
│
├── school_core/
│   ├── decorators.py                # Custom @logdecorator for JSON logging
│   └── errors.py                    # Custom exception classes
│
├── school_data/
│   ├── log.json                     # Operation logs
│   ├── student_info.pickle            # Saved student data
│   └── grades.csv                   # CSV log of grade changes
│
└── README.md                        # Documentation


## Example
```python
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

```
# 🧾 Log File Example (log.json)
```text

[
  {
    "time": "2025-11-03 18:42:22",
    "owner": "John",
    "function_name": "decrease_grade",
    "args": ["Student John by age 22 ,grade is 20", 6],
    "result": 14,
    "status": "SUCCESS"
  },
  {
    "time": "2025-11-03 18:43:10",
    "owner": "Winter School",
    "function_name": "add_student",
    "args": ["<Student Zahra>"],
    "status": "SUCCESS"
  }
]
```
# 🔮 Future Improvements
- Implement a command-line or GUI interface
- Add more detailed validation and exception handling
- Unit testing for decorators and file handling 
- More detailed report generation (average per class, ranking, etc.)
-🗄️ Optional database backend (SQLite)
- 
#  👩‍💻 Author
Zahra Betvan
Learning Python step by step with a focus on OOP design, clean code, and modular architecture.