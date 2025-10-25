from datetime import datetime
def logdecorator(func):
    def wrapper(*args, **kwargs):
        time=datetime.now()
        result=func(*args, **kwargs)
        with open("log.txt","a") as f:
            f.write("name of the function-->"+func.__name__+"\n")
            f.write(f"{time}\n")
            f.write(f"result: {result}\n")
            f.write(f"args: {args}\n")
            f.write(f"kwargs: {kwargs}\n")
            f.write("-"*50)
        return  result
    return wrapper



class Student:
    def __init__(self,name,age,grade):
        self._name = name
        self._age = age
        self._grade = grade

    @classmethod
    @logdecorator
    def from_string(cls,student_str):
        name,age,grade = student_str.split('-')
        return cls(name,int(age),int(grade))

    @staticmethod
    def is_valid_grade(grade):
        return 0<=grade<=20
    @staticmethod
    def is_valid_age(age):
        return 0<=age

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, new_grade):
        if not isinstance(new_grade, (int, float)) or new_grade < 0 or new_grade > 20:
            raise ValueError("Grade must be between 0 and 20")
        self._grade = new_grade

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,new_age):
        if new_age<0:
            raise ValueError("error --> age can not be negative")
        else:
            self._age=new_age


    def __str__(self):
        return f"{self._name} | Age: {self.age} | Grade: {self.grade}"

# ---------------------------------------------------------------------

class School:
    def __init__(self,name):
        self._name = name
        self.students = []


    @logdecorator
    def add_student(self,student):
        if not student in self.students:
            self.students.append(student)
        else:
            raise ValueError("This student already exists!")
    @logdecorator
    def remove_student(self,name):
        for student in self.students:
            if student._name==name:
                self.students.remove(student)
                break
        else:
            raise ValueError("This student doesn't exist!")

    def find_student(self,name):
        for student in self.students:
            if student.name.lower()==name.lower():
                return student
        else:
            raise ValueError("This student doesn't exist!")

    def show_students(self):
        print(f"In this school-->{self._name}:")
        if self.students:
            for student in self.students:
                print(student)
        else:
            print("No students")
    @logdecorator
    def average_grade(self):
        if not self.students:
            raise ValueError("No students so average is ZERO")
        total = sum(student.grade for student in self.students if isinstance(student.grade, (int, float)))
        return round(total / len(self.students), 2)


s1=Student("John",22,20)
s2=Student("Zahra",28,20)
s3=Student.from_string("fati-23-19")
s1.grade=20
s1.age=9
print(s1)
school=School("Winter school")
school.add_student(s1)
school.add_student(s2)
school.add_student(s3)
school.show_students()
print("*"*70)
print(school.average_grade())


