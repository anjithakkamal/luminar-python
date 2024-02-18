# 8.How to count the number of upper and lowercase letters in a string 
Str="LuMinar TechnoLab"
lower=0
upper=0
for i in Str:
	if(i.islower()):
			lower+=1
	else:
			upper+=1
print("The number of lowercase characters is:",lower)
print("The number of uppercase characters is:",upper)
