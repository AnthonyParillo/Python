weight = input('What is your weight(kg)?\n')
height = input('What is your height(m)?\n')

bmi = int(weight) / float(height) ** 2

print('Your BMI is:')
print(int(bmi))