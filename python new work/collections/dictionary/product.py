#product code,name,category,price
product={"code":123,"name":"dell","category":"lap","price":"45000"}
print("product name :-",product["name"])
#add color
product["color"]="black"
print("product color add =",product)
#upadte
product["price"]=40000
print("update price =",product)
#check offer in the dictionary
print("check offer in the dictionary =","offer" in product)
#add offer as 300 if offer key is not present else update offer as 250
if "offer" in product:
    product["offer"]=250
else:
    product["offer"]=300
print("product offer =",product)