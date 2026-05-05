# Write a Python program to create a calculator using functions. 
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b
# Get user input for the operation and numbers
operation = input("Enter operation (add, subtract, multiply, divide): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
# Perform the operation based on user input
if operation == "add":
    result = add(num1, num2)
elif operation == "subtract":
    result = subtract(num1, num2)
elif operation == "multiply":
    result = multiply(num1, num2)
elif operation == "divide":
    result = divide(num1, num2)
else:
    result = "Invalid operation"
# Print the result
print("Result:", result)

    