def add_numbers(*args):#(*tuple)
    return sum(args)
print("add numbers :-",add_numbers(10,20,30,40))
print("add numbers :-",add_numbers(10,20))

def display_mobile_detail(**kwargs):#(**dictionary)
    print("mobile name :-",kwargs.get("name"))
display_mobile_detail(name="realmec35",brand="realme",price="14500")