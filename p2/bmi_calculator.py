# BMI Calculator
# -----------------------

height = float(input('please enter your height in metres: '))
weight = float(input('please enter your weight in kgs: '))
bmi = weight/(height * height)
print(int(bmi))