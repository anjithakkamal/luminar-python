class GrandParent:
    def m1(self):
        print("inside grandparent m1 method")
class Parent:
    def m1(self):
        print("inside parent m1 method")
class Child(GrandParent,Parent):
    pass
ch=Child()
ch.m1()