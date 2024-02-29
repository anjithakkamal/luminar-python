class GrandParent:
    def m1(self):
        print("grand parent m1 method")
class parent:
    def m2(self):
        print("parent m2 method")
class child(parent,GrandParent):#multiple inheritance
    def m3(self):
        print("child m3 method")
ch=child()
ch.m3()
ch.m2()
ch.m1()
