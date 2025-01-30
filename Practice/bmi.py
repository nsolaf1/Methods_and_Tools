# < 18.5	Underweight
# 18.5 - 24.9	Normal weight
# 25 - 29.9	 Overweight
# 30 - 34.9	 Obesity Class I
# 35 - 39.9 	Obesity Class II
# ≥ 40	 Obesity Class III (Severe)

# bmi weight / hight **2 

height = int(input("Enter Height: "))
weight = int(input("Enter Weight: "))

bmi = weight/ (height / 100) **2

print(bmi)

if bmi < 18.5:
    print("underweight")
elif  bmi < 24.9:
    print("normal")
elif bmi < 29.9:
    print("Overweight")
elif bmi < 34.9:
    print("OVER OVER WEIGHT")
else:
    print("SUPER")