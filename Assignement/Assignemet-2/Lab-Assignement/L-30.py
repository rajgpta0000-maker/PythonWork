#  Write a Python program to create a lambda function with one expression.
# Create a lambda function to calculate the square of a number
square = lambda x: x ** 2
# Get user input for a number
number = float(input("Enter a number: "))
# Call the lambda function with the user input and print the result
result = square(number)
print("The square of the number is:", result)

