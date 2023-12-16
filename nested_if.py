weight = int(input("weight in kg:"))
height = float(input("height in meters:"))

bmi = round((weight / height ** 2), 1)

if bmi < 16.0:
    print("Underweight (Severe thinness)")
elif bmi < 16.9:
    print("Underwight (Moderate thinness)")
elif bmi < 18.4:
    print("Underweight(Mild thinness)")
elif bmi < 24.9:
    print("Normal range")
elif bmi < 29.9:
    print("Overwight (Pre-obese)")
else:
    print("Obese")