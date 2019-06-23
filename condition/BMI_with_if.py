mass = float(input("enter your weight in kg plz:\n"))
height = float(input("enter your height in meter plz:\n"))
bmi = (mass) /(height**2)
print(bmi)
if bmi<18:
    print("Underweight")
elif bmi<25:
    print("Normal")
elif bmi<30:
    print("overweight")
else:
    print("obese")