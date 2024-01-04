# find bmi
# <18 underweight
# 18-25 healthy
# 25-30 over weight
# 30-35 Obese
# above 35 severe obesity

weight_in_kg=int(input("enter weight="))
height_in_cm=int(input("enter height="))
height_in_meter=height_in_cm/100
bmi=weight_in_kg//(height_in_meter)**2
print(bmi)
if(bmi<18):
    print("under weight")
elif(bmi<25):
    print("healthy")
elif(bmi<30):
    print("over weight")
elif(bmi<35):
    print("obese")
elif(bmi>=35):
    print("severe obesity")