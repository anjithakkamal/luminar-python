path="C:\\Users\\HP\\Desktop\\MY PYTHON\\file operations\\orders.txt"
f=open(path,"r")
items=[]
for line in f:
    data=line.strip("\n")
    items.append(data)
print("order list of a day ;- ",set(items))
wc={i:items.count(i) for i in set(items)}
print("orders count :- ",wc)
value_key_list=[(v,k) for k,v in wc.items()]
print("maxmimum order :-",max(value_key_list))
print("minimum order :- ",min(value_key_list))
print("sorted order:- ",sorted(value_key_list,reverse=True))
# print("sorted order:- ",sorted(value_key_list))
