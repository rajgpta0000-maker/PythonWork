# ) Write a Python program to create a parameterized function that takes two arguments and prints their sum. 
def sum_of_numbers(num1, num2):
    return num1 + num2
# Get user input for the two numbers
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
# Call the function with the user input and print the result
result = sum_of_numbers(number1, number2)
print("The sum of the two numbers is:", result)
