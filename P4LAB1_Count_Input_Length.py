input = input("Enter any text to count the number of characters in it: ")

# Declaring and initializing the counter outside of the loop
counter = 0

# Iterating through the input and counting the characters while skipping spaces, commas, and periods 
for x in input:
    if x != " " and x != "," and x !=".":
        counter += 1

print("There are {0} characters in your text".format(counter))
