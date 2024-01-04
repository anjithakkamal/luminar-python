#fibanocci series max 100 not value
prev=0
current=1
limit=100
next=1
print(prev)
print(current)
while(next<=limit):
    print(next)
    prev=current
    current=next
    next=current+prev
