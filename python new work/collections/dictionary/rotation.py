arr=[1,2,3,4,5,6,7]
#k=2
#1st=7,1,2,3,4,5,6
#2snd=6,7,1,2,3,4,5
k=2
for i in range(0,k):
    last_element=arr.pop()
    arr.insert(0,last_element)
print(arr)
