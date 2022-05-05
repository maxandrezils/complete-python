# tip_calc.py
print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))
tip = float(input('What percentage tip would you like to give: 10, 12 or 15? '))
split = int(input('How many guests were there? '))
individual_bill = round((total*(1+tip/100))/split, 2)
print(individual_bill)