# check wthr given  number is exist in fibanocci number
num=int(input("enter number="))
is_fibo=False
prev=0
current=1
next=prev+current
while(next<=num):
    if next==num:
        is_fibo=True
        break
    prev=current
    current=next
    next=prev+current
print(is_fibo)
        

