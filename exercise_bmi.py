weight = input("Enter weight in kg:")
height = input("Enter height in meters:")

BMI = round((int(weight) / float(height) ** 2), 2)

print("\nBMI is " + str(BMI))