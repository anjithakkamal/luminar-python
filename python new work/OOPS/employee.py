class Employee:
    emp_code:str
    name:str
    dept_name:str
    salary:int
    def set_employee(self,code,name,dept_name,salary):
        self.emp_code=code
        self.name=name
        self.dept_name=dept_name
        self.salary=salary
    def display(self):
        print(self.emp_code,self.name,self.dept_name,self.salary)
obj1=Employee()
obj1.set_employee("E123","Anji","hr",45000)
obj1.display()
obj2=Employee()
obj2.set_employee("E124","Merin","IT",47000)
obj2.display()