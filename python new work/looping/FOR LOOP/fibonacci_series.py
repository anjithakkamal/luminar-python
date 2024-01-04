#fibanocci series
prev=0
current=1
print(prev)
print(current)
for i in range(0,10):
    next=prev+current
    print(next)
    prev=current
    current=next