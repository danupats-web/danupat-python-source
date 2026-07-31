weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))

bmi = weight / (height ** 2)

print("BMI:", round(bmi, 1))

if bmi < 18.5:
    print("Underweight")
elif bmi <= 24.9:
    print("Normal weight")
elif bmi <= 29.9:
    print("Overweight")
else:
    print("Obese")