# Basic Math Operations
# 11/30/2020
# CTI-110 P2HW1 - Meal Tip Tax Calculator
# Gabriel Khachatryan

print("This program will calculate the tip and the tax for your meal.")

# Prompt the user to input data
print("Enter the charged amount for the meal")
charge = float(input())

# Prompt the user to enter the percentage of intended tip
print("What percent of tip should be calculated?")
tipRate = float(input())/100

# Prompt the user to enter the tax rate
print("What is the tax rate?")
taxRate = float(input())/100

# Calculate the tip and the tax amounts
tip = charge * tipRate
tax = charge * taxRate

# Display the calculated tip, tax, and the total cost of the meal
print("tip: $", '{:.2f}'.format(tip), sep="")
print("tax: $", '{:.2f}'.format(tax), sep="")
print("total charge: $", '{:.2f}'.format(charge + tip + tax), sep="")

