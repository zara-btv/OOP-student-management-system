import csv
import os
import datetime
from school_core.errors import AmountValueError, NegativeValueError, ValueTypeError
from school_core.decorators import logdecorator

class Student:
    def __init__(self, name, age,grade):
        self._name = name
        self._age = age
        self._grade = grade
        self._backup_grade=grade
    def __enter__(self):
        print(f"Start Action on {self._name}'s grade!")
        self._backup_grade = self._grade
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"Error occurred: {exc_val} . Rolling back grade... ")
            self._grade=self._backup_grade
            return self._grade
        else:
            print(f"End Action on {self._name}'s grade! SUCCESSFULLY!")
            return False


    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if value.isalpha():
            self._name = value
        else:
            raise ValueTypeError("Enter your name not your phone number !")
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if int(value) < 0:
            raise NegativeValueError("Enter your age and it should not be negative !")
        self._age = value

    @property
    def grade(self):
        return self._grade
    @grade.setter
    def grade(self, value):
        if not (0<value<=20 ):
            raise AmountValueError("Grade must be between 0 and 20")
        self._grade=value
    @logdecorator
    def add_to_grade(self,amount):
        if amount<0:
            raise NegativeValueError("Grade must be greater than 0")
        self._grade+=amount
        if self._grade>20:
            raise AmountValueError("Grade must not be greater than 20")
        with open("./school_data/grades.csv","a",newline="",encoding="utf-8") as f:
            fieldnames=["Name","Age","Action","Grade","Date"]
            writer = csv.DictWriter(f,fieldnames=fieldnames)
            if f.tell()==0:
                writer.writeheader()
            writer.writerow({"Name":self._name,"Age":self._age,"Action":"improve the grade","Grade":self._grade,"Date":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        return self._grade
    @logdecorator
    def decrease_grade(self,amount):
        if amount<0:
            raise NegativeValueError("Grade must be greater than 0")
        self._grade-=amount
        if self._grade<0:
            raise NegativeValueError("Grade must not be less than 0")
        os.makedirs("./school_data",exist_ok=True)
        with open("./school_data/grades.csv", "a", newline="", encoding="utf-8") as f:
            fieldnames=["Name","Age","Action","Grade","Date"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if f.tell() == 0:
                writer.writeheader()
            writer.writerow({"Name": self._name, "Age": self._age, "Action": "reduce the grade", "Grade": self._grade,
                             "Date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})

        return self._grade
    @classmethod
    def new_stu(cls,new_student):
        name,age,grade=new_student.strip().split("-")
        return cls(name,age,int(grade))
    def __str__(self):
        return f"Student {self._name} by age {self._age} ,grade is {self._grade}"
    def __repr__(self):
        return self.__str__()

    def to_dict(self):
        return {"name":self._name, "age":self._age, "grade":self._grade}