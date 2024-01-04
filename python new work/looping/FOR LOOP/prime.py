#print all prime numbers from 40 to 100
n1=40
n2=100
print("----print all prime numbers from 40 to 100----")
if n1<n2:
    for i in range(n1,n2+1):
        for j in range(2,n2+1):
            if i%j==0:
                break
        if i==j:
            print(i)
#             # else:
#             #     print("invalid")
# range1=40
# range2=100
# for i in range(40,100):
#     for j in range(2,100):
#             if(i%j==0):
#                 break
#             if i==j:
#                 print(i)
