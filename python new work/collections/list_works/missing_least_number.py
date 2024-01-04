# list=[4,5,2,1,3]
# list.sort()
# print("list in sorted order is:-",list)
# list_max=max(list)
# for i in range(1,list_max):
#     if i not in  list: 
#         print("misiing least number is:-",i) 
arr=[1,3,4,5]
arr.sort()
left=0
while(left<len(arr)-1):
    right=left+1
    r_element=arr[right]
    l_element=arr[left]

    if r_element-l_element!=1:
        print(l_element+1,"is missing")
        break
    else:
        left=left+1
else:
    print(r_element+1,"is missing")