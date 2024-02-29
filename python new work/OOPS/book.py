class Book:
    title:str
    author:str
    price:int
    pages:int
    def __str__(self):#string representaion of an object
        return self.title
    def __init__(self,title,author,price,pages):
        self.title=title
        self.author=author
        self.price=price
        self.pages=pages
obj1=Book("randamoozham","mt",550,480)
obj2=Book("arachar","meera",650,480)
print(obj1)
        