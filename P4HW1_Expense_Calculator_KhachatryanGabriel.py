# Expense Calculator
# 12/06/2020
# CTI-110 P4HW1 Expense Calculator 
# Gabriel Khachatryan

# prompt the user to enter the amount in account 
startingBalance = int(input("What is the account balance? "))

# declaring and initializing the running balance
runningBalance = startingBalance

# declaring and initializing the variables needed to run the process
expense = 0
expenseCount = 0
keep_going = 'y'

while keep_going.lower() == 'y':
    # prompt the user to enter the amount of each expense
    expense = int(input("Enter expense amount: "))
    runningBalance -= expense
    expenseCount += 1

    # promp the user for another expense
    keep_going = input('Do you want to submit another expense (Enter "Y" if so): ')

# display starting balance, number of expenses, and the ending balance
print("Starting balance: {0}\nNumber of Expenses {1}\nEnding balance: {2}".format(startingBalance, expenseCount, runningBalance))
