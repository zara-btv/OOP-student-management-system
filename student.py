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



class Student:
    def __init__(self,name,age,grade):
        self._name=name
        self._age=age
        self._grade=grade
        self._backup_grade=grade
    def __enter__(self):
        print(f"Starting Transaction for Student {self._name}")
        self._backup_grade=self._grade
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
                print(f"⚠️ Error occurred: {exc_val}. Rolling back ...")
                self._grade = self._backup_grade
                return self._grade
        else:
            print("✅ Transaction completed successfully.")
            return False

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name=name
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,age):
        if age<0:
            raise ValueError("age must be positive")
        self._age=age

    @property
    def grade(self):
        return self._grade
    @grade.setter

    def grade(self,grade):
        if not 0<=grade<=20:
            raise ValueError("grade must be between 0 and 20")
        self._grade=grade

    @logdecorator
    def set_grade(self, grade):
        self.grade = grade
        return self.grade

    @classmethod
    def new_stu(cls,new_student):
        name,age,grade=new_student.strip().split("-")
        return cls(name,int(age),float(grade))
