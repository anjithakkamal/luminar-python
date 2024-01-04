#leap year from 1800- 2024 using for loop
for i in range(1800,2024):
    if(i%100==0 and i%400==0) or (i%100!=0 and i%4==0):
        print(i)
