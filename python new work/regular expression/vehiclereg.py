from re import *
vehicle_number="KL-05-TH-6479"
rule="(KL)[-]?[0-9]{2}[-]?[A-Z]{1,2}[-]?[0-9]{4}"     #[-]? for '-?'is optional
# rule="(KL)[0-9]{2}[A-Z]{1,2}[0-9]{4}"
matcher=fullmatch(rule,vehicle_number)
print("invalid" if matcher == None else "valid")