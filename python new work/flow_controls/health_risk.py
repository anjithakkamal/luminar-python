#-----------WOMEN-----------
# 0.80 OR BELOW  = LOW
#0.81 TO 0.85    = MODERATE
# 0.85+          = HIGH
#--------MEN--------------
# 0.95 OR BELOW  = LOW
#0.96 TO 1.0    = MODERATE
# 1.0+          = HIGH

tummy_size=int(input("enter the tummy size ="))
buttock_size=int(input("enter the buttock size ="))
gender=input("enter gender :")
value=tummy_size/buttock_size
value=round(value,2)
print(value)
# if gender == "female":
# if(value<0.80 and gender=="female")or(value<0.95 and gender=="male"):
#     print("health risk is low")
# elif(value>0.85 and gender=="female")or(value<1.0 and gender=="male"):
#     print("health risk is moderate")
# elif(value>=0.85 and gender=="female") or(value>=1.0 and gender=="male"):
#     print("health risk is high")



if(gender=="male"):
    if(value<=.95):
        print("health risk is low")
    elif(value<=1.0):
        print("health risk is moderate")
    elif(value>1.0):
        print("health risk is high")
elif(gender=="female"):
    if(value<=.80):
        print("health risk is low")
    elif(value<=.85):
        print("health risk is moderate")
    elif(value>.85):
        print("health risk is high")