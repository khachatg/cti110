# Save mile pre gallon input
mpg = float(input())

# Save dollars per gallon (gas price) input
dpg = float(input())

# Calculate and display gas costs for 20 miles, 75 miles, and 500 miles
print('{:.2f} {:.2f} {:.2f}'.format(20/mpg * dpg, 75/mpg * dpg, 500/mpg * dpg))
