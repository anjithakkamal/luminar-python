from re import *
vehicle_number="KL05TH6479"
rule="(KL)[0-9]{2}[A-Z]{1,2}[0-9]{4}"
matcher=fullmatch(rule,vehicle_number)
print("invalid" if matcher == None else "valid")