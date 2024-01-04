 
# Calculate Monthly EMI 
# Total Interest Payable
# Total Payment(Principal + Interest)
# EMI=(p*r*(1+r)**n)/((1+r)**n-1)
# p=principal or loan loan_amount
# r= interest rate per month
# n=number of monthly installment
# monthly interest rate(r)=R/(12*100)


loan_amount=200000
interest_rate=9
tenure=20
n=tenure*12
r=interest_rate/(12*100)
# r=monthly interest rate
# --------CALCULATE MONTHLY EMI-------
emi=(loan_amount*r*(1+r)**n)/((1+r)**n-1)
print("Monthly emi is  = " , emi)

# ---------TOTAL INTEREST PAYABLE----------
total_interest=emi*n-loan_amount
print("Total interest payable =" ,total_interest)

#  ------------TOTAL PAYMENT-----------
total_payment=loan_amount+total_interest
print("Total Payment =" ,total_payment)

# total_interest_payable=loan_amount*tenure*interest_rate/100
# total_payment=loan_amount+total_interest_payable
# emi=total_payment/(tenure*12)
# print("Monthly emi is =", emi)