from re import fullmatch
pan_card="DTZPS6463J"
#first 3 characters from A to Z
#4th place P,C,A,F,H,T
#STH Place aplhabet
#followed by 4 digit
#alphabet in last place
rule="[A-Z]{3}[PCAFHT]{1}[A-Z]{1}[0-9]{4}[A-Z]{1}"
matcher=fullmatch(rule,pan_card)
if(matcher!=None):
    print("valid")
else:
    print("invalid")