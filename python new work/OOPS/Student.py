class Student:#constructor __init__()
    name:str
    course:str
    degree:str
    def __init__(self,name,course,degree):#method
        self.name=name
        self.course=course
        self.degree=degree
    def display(self):
        print(self.name,self.course,self.degree)
obj1=Student("Anji","Django","MCA")#object
obj1.display()
obj2=Student("Merin","Django","MCA")
obj2.display()