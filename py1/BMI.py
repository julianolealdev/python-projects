print("This is a BMI calculator, put your datas to discover your category") 
weight = int(input("Enter your weight: "))
alt = float(input("Enter your height in meters: "))

a = alt ** 2

print("height:",alt,"weight:",weight)
sum = weight / a
print(sum)

if sum < 18.5:
    print("Your BMI is in the THIN category")
elif sum > 18.6 and sum < 24.9:
    print("Your BMI is in the NORMAL category")
elif sum > 25 and sum < 29.9:
    print("Your BMI is in the OVERWEIGHT category")
elif sum > 30 and sum < 34.9:
    print("Your BMI is in the OBESITY I category")
elif sum > 35 and sum < 39.9:
    print("Your BMI is in the OBESITY II category")
else: 
    print("Your BMI is in the OBESITY III category")
