# st={10,20,30,10,10,"hello",True}
# print(st)
#---------------SET METHODS---------------
#1)add()
st={10,20,30,40,"hello"}
st.add(50)
print("add number to the set=",st)
#2)pop()
st.pop()
print("fremove one element in the set",st)
#3)remove()
st.remove(10)
print("remove in the set",st)
#4)discard()
st.discard(10)
print("discard =",st)
#5)union
set1={10,20,30,40,37}
set2={20,30,40,50}
union_set=set1.union(set2)
print("union of set =",union_set)
#6)intersection
intersection_set=set1.intersection(set2)
print("intersection of set =",intersection_set)
#7)difference
difference_set=set1.difference(set2)
print("difference of set 1 - set 2 =",difference_set)
difference_set=set2.difference(set1)
print("difference set 2 - set 1",difference_set)
#8)update
colors={"red","green","blue"}
new_set={"cyan","purple","brown"}
colors.update(new_set)
print("update =",colors)
