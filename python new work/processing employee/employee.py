from json import load
path="C:\\Users\\HP\\Desktop\\MY PYTHON\\processing employee\\data.json"
f=open(path,"r")
employees=load(f)
print(employees)

#1) no of employees
print("no of employees :-",len(employees))

#2)print all employee name
employee_name=[e.get("name") for e in employees]
print("employees name :- ",employee_name)

#3)employee name working as qa
employee_working=[e.get("name") for e in employees if e.get("department")=="qa"]
print("employees of qa department :- ",employee_working)

#4) employee working at ekm
employee_working_ekm=[e.get("name") for e in employees if e.get("location")=="ekm"]
print("employees  working at ekm :- ",employee_working_ekm)

