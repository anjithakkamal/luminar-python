# most_frequest_list=max(list.count)
# print(most_frequest_list)
# Program to find most frequent element in a list
list=[1,2,3,4,4,5,6,6,6,7]
def most_frequent(list):
	counter = 0
	num = list[0]
	
	for i in list:
		curr_frequency = list.count(i)
		if(curr_frequency> counter):
			counter = curr_frequency
			num = i
	return num
print("most frequent number in the list is :-",most_frequent(list))
