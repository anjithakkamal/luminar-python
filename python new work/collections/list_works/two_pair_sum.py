#2 pair sum
# sum=8(3,5)
# sum=6(4,2)
arr=[2,3,5,4]
sum=8
# sum=int(input("enter number="))
is_present=False

for i in range(0,len(arr)-1):
    for j in range(i+1,len(arr)):
        i_element=arr[i]
        j_element=arr[j]
        cur_sum=i_element+j_element
        if sum==cur_sum:
            print("pairs",i_element,j_element)
            is_present=True
            break
if is_present==False:
    print("no pairs exit")