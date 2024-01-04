lst=[1,2,4,5,6]
print("list=",lst)
squares=[num**2 for num in lst]
print("squares=",squares)
cubes=[num**3 for num in lst]
print("cubes=",cubes)
add_five=[num+5 for num in lst]
print("add five=",add_five)
odd=[num for num in lst if num%2!=0]
print("odd numbers in the list=",odd)
even=[num for num in lst if num%2==0]
print("even number in the list=",even)

languages=["python","c++","java","javascript","typescript"]
new_list=[lang.upper() for lang in languages]
print("upper case =",new_list)

len_filter=[lang for lang in languages if len(lang)>5]
print("length filter in the list =",len_filter)

#if num>5 return num+1 if num<5 return num-1
lst=[2,4,6,3,1]
mapped_nums=[num+1 if num>5 else num-1 for num in lst]
print("mapped nums =",mapped_nums)


lst=["+","-","+","+","-","-"]
map_symbols=[1 if sym=="+" else 0 for sym in lst]
print("mapped symbols",map_symbols)

