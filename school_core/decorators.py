from datetime import datetime
import json
from json import JSONDecodeError


def logdecorator(func):
    def wrapper(*args, **kwargs):
        time = datetime.now()
        name=args[0].name if args else "Unknown"
        try:
            result=func(*args, **kwargs)
            log_status="SUCCESS"
        except Exception as e:

            result=str(e)
            log_status=f"Exception occurred:{type(e).__name__}"
            backup=getattr(args[0],"_backup_grade",None)
            log_entry={
                "time":str(time.hour)+":"+str(time.minute)+":"+str(time.second)+"/"+str(time.date()),
                "name":name,
                "func":func.__name__,
                "args":[str(a) if not isinstance(a,(int,float,str)) else a for a in args],
                "status":log_status,
                "exception":str(e),
                "Rollback":backup
            }
            try:
                with open("school_data/log.json","r",encoding="utf-8") as f:
                    logs=json.load(f)
                    if isinstance(logs,dict):
                        logs=[logs]
            except(FileNotFoundError,JSONDecodeError):
                logs=[]
            logs.append(log_entry)
            with open("school_data/log.json","w",encoding="utf-8") as f:
                json.dump(logs,f,indent=4,ensure_ascii=False)
            raise
        else:
            log_entry={
                "time":str(time.hour)+":"+str(time.minute)+":"+str(time.second)+"/"+str(time.date()),
                "name":name,
                "func":func.__name__,
                "args":[str(a) if not isinstance(a,(int,float,str)) else a for a in args],
                "status":log_status,
                "result":result,

            }
            try:
                with open("school_data/log.json","r",encoding="utf-8") as f:
                    logs=json.load(f)
                    if isinstance(logs,dict):
                        logs=[logs]
            except(FileNotFoundError,JSONDecodeError):
                logs=[]
            logs.append(log_entry)
            with open("school_data/log.json","w",encoding="utf-8") as f:
                json.dump(logs,f,indent=4,ensure_ascii=False)
            return result
    return wrapper





