arr=[2,3,6,4]
arr.sort()
left=0
right=len(arr)-1
sum=11
is_present=False
while(left<right):
    l_element=arr[left]
    r_element=arr[right]
    curr_sum=l_element+r_element
    if sum==curr_sum:
        print("pairs",l_element,r_element)
        is_present=True
        break
    elif sum>curr_sum:
        left=left+1
    elif sum<curr_sum:
        right=right-1
if is_present==False:
    print("no pair exist")
        

