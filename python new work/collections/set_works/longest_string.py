lst=[10,20,30,20,20,40,20]
st=set(lst)
print("number repeat =",st)
###################################################
all_users={"sachin","dravid","laxman","jadeja","dhoni","raina"}
dhoni_friends={"sachin","raina"}
suggestion_set=all_users.difference(dhoni_friends)
suggestion_set.discard("dhoni")
print("suggestion set =",suggestion_set)
##############################
all_students={"hari","tom","john","vipin","vinu"}
failed_students={"tom","john"}
passed_students=all_students.difference(failed_students)
print("passed students =",passed_students)

