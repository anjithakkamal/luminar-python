#def is_leap year (year) return true if year is leap year else return false
def is_leapyear(year):
    if(year%100==0 and year%400==0) or (year%100!=0 and year%4==0):
        return True
    else:
        return False
print(is_leapyear(2024))