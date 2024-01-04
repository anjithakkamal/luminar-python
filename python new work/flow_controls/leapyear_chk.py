year=int(input("enter year"))
if(year%100==0 and year%400==0) or(year%100!=0 and year%4==0):
    print("year is leap year")
else:
    print("year is not leap year")