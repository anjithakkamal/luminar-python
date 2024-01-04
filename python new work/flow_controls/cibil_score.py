#<550=poor
# 550-650=average
# 650-750=good
# >750=excellent
# cibil_score=int(input("enter cibil score="))
# if(cibil_score<550):#0-549
#     print("poor")
# elif cibil_score>=550 and cibil_score<650:#649>=500 and 649<650 t& t
#     print("average")
# elif cibil_score>650 and cibil_score<750:
#     print("good")
# elif cibil_score>=750:
#     print("excellent")
 
cibil_score=int(input("enter cibil score="))
if(cibil_score<550):
     print("poor")
elif(cibil_score<650):
    print("average")
elif(cibil_score<750):
    print("good")
elif(cibil_score>=750):
    print("excellent")