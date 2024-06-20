let loan_amount=200000
let interest_rate=9
let tenure=20
n=tenure*12
r=interest_rate/(12*100)
emi=(loan_amount*r*(1+r)**n)/((1+r)**n-1)

console.log(`monthly  emi is:${emi}`);