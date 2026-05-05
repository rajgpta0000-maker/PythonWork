#  Write a Python program to create a lambda function with two expressions. 
# Create a lambda function to calculate the sum and product of two numbers
sum_product = lambda x, y: (x + y, x * y)
# Get user input for the two numbers
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
# Call the lambda function with the user input and print the results
sum_result, product_result = sum_product(number1, number2)
print("The sum of the two numbers is:", sum_result)
print("The product of the two numbers is:", product_result)
