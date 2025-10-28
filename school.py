from datetime import datetime

class NegativeValueError(Exception):
    pass

def logdecorator(func):
    def wrapper(*args, **kwargs):
        time=datetime.now()
        if hasattr(args[0], 'name'):
            owner = args[0].name
        elif hasattr(args[0], '_name'):
            owner = args[0]._name
        else:
            owner = "Unknown"
        try:
            result=func(*args, **kwargs)
            log_status="SUCCESS"
        except Exception as e:
            result=str(e)
            log_status=f"Exception ({type(e).__name__})"
            backup=getattr(args[0],"_backup_grade",None)
            with open("log.txt","a",encoding="utf-8") as f:
                f.write(f"\ntime--->{time}\n")
                f.write(f"owner--->{owner}\n")
                f.write(f"function name--->{func.__name__}\n")
                f.write(f"Status--->{log_status}\n")
                f.write(f"Exception--->{e}\n")
                if backup is not None:
                    f.write(f"rollback balance: {backup}\n")
                f.write("-"*100)
            raise
        else:
            with open("log.txt","a",encoding="utf-8") as f:
                f.write(f"\ntime--->{time}\n")
                f.write(f"owner--->{owner}\n")
                f.write(f"function name--->{func.__name__}\n")
                f.write(f"Status--->{log_status}\n")
                f.write(f"grade--->{result}\n")
                f.write("-"*100)
            return result
    return wrapper





class School :
    def __init__(self,name):
        self._name=name
        self.students=[]
    @logdecorator
    def add_student(self,student):
        if not any(s.name==student.name for s in self.students):
            self.students.append(student)
        else:
            raise ValueError("Student already added")
    @logdecorator
    def remove_student(self,student):
        if student in self.students:
            self.students.remove(student)
        else:
            raise ValueError("Student not found")
    def show_students(self):
        print(f"school name with {self._name} : ")
        if self.students:
            for student in self.students:
                print(f"name-->{student.name} \nage--> {student.age} \ngrade-->{student.grade} \n ----- ")
        else:
            raise ValueError("No students so average is ZERO")
    def show_history(self):
        print("\n📜 Transaction History:\n" + "-" * 60)
        with open("log.txt", "r", encoding="utf-8") as file:
            print(file.read())
    def average_grade(self):
        if not self.students:
            raise ValueError("No students so average is ZERO")
        total=sum(student.grade for student in self.students if isinstance(student.grade ,(int,float)))
        return round(total/len(self.students),2)

