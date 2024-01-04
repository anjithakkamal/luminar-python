#linear search
arr=[1,4,6,7,8,15,20]
element=15
for num in arr:
    if element==num:
        print("element found")
        break
else:
    print("element not found")
