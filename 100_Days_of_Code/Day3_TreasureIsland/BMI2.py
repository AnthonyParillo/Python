weight = float(input('What is your weight(kg)?\n'))
height = float(input('What is your height(m)?\n'))

bmi = format(weight / height ** 2, ".2f")

print(f'Your BMI is: {bmi}')

bmi = weight / height ** 2

if bmi < 18.5:
  print("You are: UNDERWEIGHT")
elif bmi < 25:
  print("You are: NORMAL WEIGHT")
elif bmi < 30:
  print("You are: OVERWEIGHT")
elif bmi < 35:
  print("You are: OBESE")
else:
  print("You are: CLINICALLY OBESE")