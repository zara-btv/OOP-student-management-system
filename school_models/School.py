import pickle

from school_core.decorators import logdecorator
from school_models.Student import Student
import json
class School:
    def __init__(self,school_name):
        self.name=school_name
        self._school_students=[]
    @logdecorator
    def add_student(self,student):
        if not any(stu.name==student.name for stu in self._school_students):
            self._school_students.append(student)
        else:
            raise ValueError("Student already has a participate in this school")
    @logdecorator
    def remove_student(self,student):
        if student in self._school_students:
            self._school_students.remove(student)
        else:
            raise ValueError("Participate not in this school")
    def average_grade(self):
        if self._school_students:
            for participate in self._school_students:
                total=sum(student.grade for student in self._school_students if isinstance(student.grade,(int,float)))
                return round(total/len(self._school_students),2)
            else:
                raise ValueError("No students so average is ZERO")
    def show_participates(self):
        print(f" {self.name} school participates are:")
        if self._school_students:
            for participate in self._school_students:
                print(f" {participate.name} is attend to school. \n")
        else:
            raise ValueError("No school participates in this school")

    def save_to_json(self, filename="student_info.json"):
        data=[stu.to_dict() for stu in self._school_students]
        with open(filename,"w",encoding="utf-8") as f:
            json.dump(data,f,indent=4,ensure_ascii=False)

    @classmethod
    def load_from_json(cls,filename="student_info.json"):
        with open(filename,"r",encoding="utf-8") as f:
            data=json.load(f)
        School=cls("Happy kids")
        for stu_data in data:
            stu=Student(stu_data["name"],stu_data["age"],stu_data["grade"])
            School.add_student(stu)
        return School

    def save_pickle(self,filename="./school_data/student_info.pickle"):
        with open(filename,"wb") as f:
            pickle.dump(self._school_students,f)
    @staticmethod
    def load_pickle(filename="./school_data/student_info.pickle"):
        with open(filename,"rb") as f:
            return pickle.load(f)




