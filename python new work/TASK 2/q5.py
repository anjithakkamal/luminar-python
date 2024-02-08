# Q5: Python program to get the Fibonacci series between 0 to 50
prev=0
current=1
limit=50
next=1
print(prev)
print(current)
while(next<=limit):
    print(next)
    prev=current
    current=next
    next=current+prev
