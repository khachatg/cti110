input = input("Enter a candidate password: ")

# Declaring and initializing the varialbe that will hold the modified password value
modifiedPassword = ''

# Iterating through the input replace characters as needed
for x in input:
    if x=='i':
        modifiedPassword += '!'
    elif x=='a':
        modifiedPassword += '@'
    elif x=='m':
        modifiedPassword += 'M'
    elif x=='B':
        modifiedPassword += '8'
    elif x=='o':
        modifiedPassword += '.'
    else:
        modifiedPassword += x

print("Consider this following, stronger, password instead:", modifiedPassword)
