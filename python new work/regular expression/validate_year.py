#1800-2024
from re import fullmatch

yr="1899" #1899-1999
rule="((18|19)[0-9]{2}||20[01][0-9]|202[0-4])"
matcher=fullmatch(rule,yr)
if (matcher!=None):
    print("valid")
else:
    print("invalid")
