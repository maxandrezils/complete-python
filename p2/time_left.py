# time_left.py
# 🚨 Don't change the code below 👇
from email import message


age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
max_age = 90
years_remaining = max_age - int(age)
message = f"You have {years_remaining*365} days, {years_remaining*52} weeks, and {years_remaining*12} months left."
print(message)