# Meal, Tip Calculator
# 12/06/2020
# CTI-110 P2HW1 - Meal Tip Tax Calculator
# Gabriel Khachatryan

# Prompt the user to input data
print("Enter the charged amount for the meal")
charge = float(input())

# Prompt the user to enter the percentage of intended tip
print("What percent of tip should be calculated?\nOption 1: 15%\nOption 2: 18%\noption 3: 20%")
tipOption = int(input())

# Validate the input
while tipOption not in range(1,4):
    print("Please select a valid option")
    tipOption = int(input())

# Assign the correct tip rate based on the input option
if tipOption == 1:
    tipRate = .15
elif tipOption == 2:
    tipRate = .18
elif tipOption == 3:
    tipRate = .2

# A fixed amount of 6% sales tax will be calculated in the total 
taxRate = 0.06

# Calculate the tip and the tax amounts
tip = charge * tipRate
tax = charge * taxRate

# Display the calculated tip, tax, and the total cost of the meal
print("charge: $", '{:.2f}'.format(charge), sep="")
print("tip: $", '{:.2f}'.format(tip), sep="")
print("tax: $", '{:.2f}'.format(tax), sep="")
print("----------------------")
print("total charge: $", '{:.2f}'.format(charge + tip + tax), sep="")

