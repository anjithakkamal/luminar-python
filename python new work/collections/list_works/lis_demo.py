expenses=[15000,20000,16000,17000,12000]
print(expenses[1])#20000
#update march month exp as 18000
expenses[2]=18000
print("update march month exp as 18000",expenses)
print("-----using range----")
for i in range(0,len(expenses)):
    print(expenses[i])
print("-----using object----")
for obj in expenses:
    print(obj)
#expenses>19000
for obj in expenses:
    if obj>19000:
        print("expenses > 19000 is :-",obj)
#print exp ranges 15k-18k
for obj in expenses:
    if obj>=15000 and obj<=18000:
        print(obj)
#total expenses
total=sum(expenses)
print("total expenses=",total)
costly_expense=max(expenses)
print("costly expenses=",costly_expense)
cheapest_expense=min(expenses)
print("cheapest expenses=",cheapest_expense)


