from re import *
phone_number="9947374509"
rule="[0-9]{10}"
matcher=fullmatch(rule,phone_number)
print("invalid" if matcher == None else "valid")