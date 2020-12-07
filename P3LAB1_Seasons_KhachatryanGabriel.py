
# Declaring a list of all possible valid month values
allMonths = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
longMonths = ['january', 'march', 'may', 'july', 'august', 'october', 'december']

input_month = input("What month is it now? (enter the full name of the month) ")

# Validate the input using the list of all possible valid entries
while input_month.lower() not in allMonths:
    input_month = input("Invalid entry! {0} is not a valid month.\nPlease make a valid entry: ".format(input_month))

input_date = int(input("What date is it today? "))

# validating the value of input_date
while input_date < 0 or (input_month.lower() in longMonths and input_date > 31) or (input_month.lower() not in longMonths and input_date > 30) or (input_month.lower() == 'february' and input_date > 29):
    input_date = int(input("Invalid entry! {0} {1} is not a valid date.\nPleae make a valid entry: ".format(input_month, input_date)))

# using the provided ranges for each season determine which statement to print
if input_month.lower() == 'january' or input_month.lower() == 'february' or (input_month.lower() == 'december' and input_date >= 20) or (input_month.lower() == 'march' and input_date < 20):
    print("Winter")
elif input_month.lower() == 'april' or input_month.lower() == 'may' or (input_month.lower() == 'march' and input_date >= 20) or (input_month.lower() == 'may' and input_date < 20):
    print("Spring")
elif input_month.lower() == 'july' or input_month.lower() == 'august' or (input_month.lower() == 'june' and input_date >= 20) or (input_month.lower() == 'august' and input_date < 20):
    print("Summer")
elif input_month.lower() == 'october' or input_month.lower() == 'november' or (input_month.lower() == 'september' and input_date >= 20) or (input_month.lower() == 'december' and input_date < 20):
    print("Autumn")
