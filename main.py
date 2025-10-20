import json
class Student:
    def __init__(self,name,age,grade):
         self.name = name
         self.age = age
         self.grade = grade
    def update_grade(self,new_grade):
         self.grade = new_grade
         return self.grade
    def __str__(self):
         return f"{self.name} with age {self.age} has this {self.grade} grade."


class School:
    def __init__(self,name):
        self.name = name
        self.students = []
    def add_student(self,student):
        if any(s.name==student.name for s in self.students):
            print("Student Already Exist")
        else:
            self.students.append(student)
            print(f"{student.name} Added Successfully")
    def remove_student(self,name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                print(f"{name} has removed.")
                break
        else:
            print(f"{name} doesn't exist.")
    def find_student(self,name):
        for student in self.students:
            if student.name.lower() == name.lower():
                return student
        return None

    def average_grade(self):
        if not self.students:
            return 0
        total=sum(student.grade for student in self.students)
        return total/len(self.students)


    def save_to_file(self,filename="students.json"):
        data=[]
        for student in self.students:
            data.append({
                "name":student.name,
                "age":student.age,
                "grade":student.grade
            })
        with open(filename,"w") as file:
            json.dump(data,file,indent=4)
        print(f"Data saved to {filename}")
    def load_from_file(self,filename="students.json"):
        try:
            with open(filename,"r")as file:
                data=json.load(file)
            self.students=[]
            for items in data:
                student=Student(items["name"],items["age"],items["grade"])
                self.students.append(student)
            print(f"Data loaded from {filename}")
        except FileNotFoundError:
            print(f"File {filename} not found.")

    def show_students(self):
        print(f"in this School '{self.name}':")
        if not self.students:
            print("in this school has no students.")
        else:
            for student in sorted(self.students, key=lambda s:s.name):
                print(student)


s1=Student("James",22,18)
s2=Student("Zahra",26,20)
s3=Student("Ali",30,18)
# s1.update_grade(20)
school=School("yellow")
school.add_student(s1)
school.add_student(s2)
school.add_student(s3)
print("*"*70)
school.remove_student(s1.name)
print("*"*70)

finding=school.find_student(s1.name)
print(finding)
print("*"*70)

average=school.average_grade()
print(average)
print("*"*70)

school.save_to_file()
school.load_from_file()
print("*"*70)
school.show_students()
print("*"*70)
