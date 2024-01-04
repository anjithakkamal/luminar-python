years=[]
century_years=[]
non_century_years=[]
leap_year=[]
for y in range(1800,2025):
    years.append(y)
for y in years:
    if y%100==0:
        century_years.append(y)
    else:
        non_century_years.append(y)
print("century years",century_years)
print("non century years",non_century_years)
print("-------------LEAP YEAR-------------")

for y in years:
    if (y%100==0 and y%400==0)or(y%100!=0 and y%4==0):
        leap_year.append(y)
print("leap years:-",leap_year)
print("number of leap years in 1800-2024:-",len(leap_year))
