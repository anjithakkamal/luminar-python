# Sorting a List by frequency of occurrence in a list
list=[1,0,1,0,0,0]
counting_order=sorted(list,key=list.count,reverse=False)
print("counting order is:-",counting_order)