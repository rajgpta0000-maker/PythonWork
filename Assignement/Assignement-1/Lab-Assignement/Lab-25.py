# Q-25: Practical Example: 1) Write a Python program to skip 'banana' in a list using the continue
# statement. List1 = ['apple', 'banana', 'mango']
fruits = ['apple', 'banana', 'mango']
for fruit in fruits:
    if fruit == 'banana':
        continue
    print(fruit)
    