
num=int(input("enter number="))
def palindrome(num):
    while(True):
        if num!=0:
            orginal=num
        else:
            num=orginal
        result=""
        while(num!=0):
            digit=num%10
            result=result+str(digit)
            num=num//10
        if orginal==int(result):
            return (orginal)
        orginal=orginal+1
if num==palindrome(num):
    print("next no of apaliandromic number=",palindrome(num+1))
else:
    print("next paliandromic number=",palindrome(num))