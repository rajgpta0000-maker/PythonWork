# Write a Python program to import the math module and use functions like sqrt(), ceil(), floor(). 
import math
# Get user input for a number
number = float(input("Enter a number: "))
# Calculate the square root, ceiling, and floor of the number
sqrt_value = math.sqrt(number)
ceil_value = math.ceil(number)
floor_value = math.floor(number)
# Print the results
print("The square root of the number is:", sqrt_value)
print("The ceiling of the number is:", ceil_value)
print("The floor of the number is:", floor_value)
