# 5)	Write a program to check the given year is a leap year or not
year=int(input("Enter the Year = "))
if(year%100==0 and year%400==0)or(year%100!=0 and year%4==0):
    print("Year is Leapyear")
else:
    print("Year is Not Leapyear")
