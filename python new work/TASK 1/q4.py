# 4)	Write  a program for grade classification based on percentage 
# conditions :percentage=90
# gradeA
# percentage in between 80-90 
# grade B
# percentage in between 70-80 
# grade C 
# percentage less than 70 
# fail
mark=int(input("Enter the Mark = "))
total=int(input("Enter Total = "))
percentage=(mark/total)*100
if percentage>=90:
    print("Grade A")
elif percentage>=80:
    print("Grade B")
elif percentage >=70:
    print("Grade C")
elif percentage<70:
    print("Fail")