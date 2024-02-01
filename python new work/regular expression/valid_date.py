from re import fullmatch

dte="31"
rule="(0[1-9]|[12][0-9]|3[01])"
matcher=fullmatch(rule,dte)
if (matcher!=None):
    print("valid")
else:
    print("invalid")

