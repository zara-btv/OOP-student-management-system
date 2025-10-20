# 🎓 Student Management System

A simple Python OOP project that allows you to manage students in a school.
It supports adding, removing, searching, and saving student data using JSON files.

## Features
- Add / remove students
- Update grades
- Search by name
- Calculate average grade
- Save and load data from `students.json`

## Example
```python
school = School("Yellow School")
s1 = Student("James", 22, 18)
school.add_student(s1)
school.save_to_file()
school.load_from_file()
school.show_students()
