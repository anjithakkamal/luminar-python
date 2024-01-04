# Write a program that prints the numbers from 1 to 100. But for multiples of three, print "abc" instead of the number, and for multiples of five,
# print "def". For numbers that are multiples of both three and five, print "abcdef".
i=1
while(i<=100):
    if(i%3==0 and i%5==0):
        print("abcdef")
    elif(i%3==0):
        print("abc")
    elif(i%5==0):
        print("def")   
    print(i)
    i=i+1