# def nextPrime():
#     num = int(input("Enter a number:"))
#     next_num = num + 1
#     while True:
#         for i in range(2, next_num):
#             if (next_num % i) == 0:
#                 next_num += 1
#             else:
#                 break

#             print("The next prime number is ",next_num)
# nextPrime();
num=int(input("enter anumber:-"))
while(True):
    i=1
    n=0
    num=num+1
    while(i<=num):
        if(num%i==0):
            n=n+1
        i=i+1
    if(n==2):
        print("next prime number is :-",num)
        break