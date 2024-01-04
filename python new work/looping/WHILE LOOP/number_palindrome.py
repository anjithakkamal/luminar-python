#paliandrome
num=121
result=""
orginal=num
while(num!=0):
    digit=num%10
    result=result+str(digit)
    num=num//10
print(result)
if(orginal==int(result)):#comparing integer
    print("number is paliandrome")
else:
    print("number is not palindrome")