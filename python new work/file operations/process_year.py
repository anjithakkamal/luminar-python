base_path="C:\\Users\\HP\\Desktop\\MY PYTHON\\file operations\\"
years_path=base_path+"years.txt"
leap_year_path=base_path+"leapyear.txt"
century_year_path=base_path+"centuryyear.txt"

year_ref=open(years_path,"r")
leap_ref=open(leap_year_path,"w")
century_ref=open(century_year_path,"w")

for line in year_ref:
    year=int(line.strip("\n"))
    if year%100==0:
        century_ref.write(str(year)+"\n")
    
    if (year%100==0 and year%400==0) or (year%100!=0 and year%4==0):
        leap_ref.write(str(year)+"\n")