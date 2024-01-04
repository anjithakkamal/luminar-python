data="this ia string"
data2='this another string method'
data3="""
this
 is 
  another 
  method 
  of 
  string"""
print(data3)

#***************STRING CLASS METHODS******************
######################METHOD CAPITALIZE()
name="hello python"
print("is capitalize:",name.capitalize())
##############CASEFOLD
name="HELLO"
print("casefold:",name.casefold())
###########isdigit()
name="123"
print("is digit:",name.isdigit())
##########isalpha()
name="hellopython"
print("is alpha:",name.isalpha())
############isalnum()
name="12"
print("isalnum:",name.isalnum())
############index(str)
name="hellopython 123"
print("index str:",name.index("el"))
##############startswirth("")
name="hellopython 123"
print("starts with:",name.startswith("he"))#case sensitive so "He" become false
###########endswith("")
name="hello python"
print("ends with=",name.endswith("on"))
##########split
name="hello python welcome"
word=name.split(",")
print("split=",word)
############count
name="hello python welcome"
print("count=",name.count(""))
#############strip
name="#hello#"
print("strip=",name.strip("#"))#remove #
##########lstrip
name="$hello$"
print("remove left strip=",name.lstrip("$"))
###########rstrip
name="$hello$"
print("remove right strip=",name.rstrip("$"))
