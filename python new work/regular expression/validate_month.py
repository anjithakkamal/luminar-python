from re import fullmatch

mnth="02"
rule="(0[1-9]|[1][012])"
matcher=fullmatch(rule,mnth)
if (matcher!=None):
    print("valid")
else:
    print("invalid")
